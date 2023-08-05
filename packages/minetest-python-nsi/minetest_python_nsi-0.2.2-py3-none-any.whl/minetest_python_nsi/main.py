#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 05 Février 2023 23:16
"""

import time
import random
import math
import os
from . import connection
from . util import *
from . blocs import BLOCS

conn = None
player = None


def connexion(pseudo: str = "", host: str = "localhost", port: int = 4711) -> tuple:
    """
    établit la connexion avec Minetest (local ou distant) et récupère l'id du joueur
    connexion(): par défaut la liaison est établie en locale

    Paramètres:
        pseudo (str, optionnel): pseudo du joueur. 
        host (str, optionnel): adresse du serveur. 
        port (int, optionnel): port. 4711 est le port par défaut 

    Renvoi:
        tuple: la connexion, l'id du joueur
    """
    global conn, player
    # Attente de connexion
    wait_for_conn = True
    while wait_for_conn:
        try:
            conn = connection.Connection(host, port)
        except:
            print("Attente de connexion...")
            time.sleep(1)
        else:
            wait_for_conn = False

    wait_for_player = True
    # connexion locale avec paramètres par défaut
    if host == "localhost":
        while wait_for_player:
            try:
                ids = conn.sendReceive("world.getPlayerIds")
            except:
                print("Attente de connexion du joueur...")
                time.sleep(1)
            else:
                wait_for_player = False

        players = list(map(int, ids.split("|")))
        player = players[0]
    else:  # connexion réseau
        while wait_for_player:
            try:
                id = conn.sendReceive("world.getPlayerId", pseudo)
                assert id != "fail", "nom de joueur inconnu"
            except:
                print("Attente de connexion du joueur...")
                time.sleep(1)
            else:
                wait_for_player = False
        player = id
    # return (conn, player)


# connexion automatique
#conn, player = connexion()
#conn, player = connexion("mon_pseudo", "mon_serveur", 4711)

# Fonctions monde


def recuperer_id_bloc(coord: tuple) -> int:
    """
    trouve l'identifiant du bloc repéré

    Paramètres:
        coord (tuple): coordonnées du bloc

    Renvoi:
        int: type de bloc
    """
    return int(conn.sendReceive("world.getBlock", intFloor(coord[0], coord[1], coord[2])))


def recuperer_nom_bloc(id: int) -> str:
    """
    trouve le nom du bloc selon son identifiant

    Paramètres:
        id (int): type de bloc

    Renvoi:
        str: nom correspondant
    """
    try:
        return BLOCS[id]["nom"]
    except KeyError:
        return "bloc inconnu"


def recuperer_nom_bloc_fr(id: int) -> str:
    """
    trouve le nom du bloc en français selon son identifiant

    Paramètres:
        id (int): type de bloc

    Renvoi:
        str: nom fr correspondant
    """
    try:
        return BLOCS[id]["nom_fr"]
    except KeyError:
        return "bloc inconnu"


def poser_bloc(coord: tuple, bloc: int, donnees: int = 0) -> None:
    """
    place un bloc aux coordonnées données
    pour certains blocs, il est possible de donner des informations supplémentaires
    (couleur, type de bois, orientation...)

    Paramètres:
        coord (tuple): coordonnées du bloc
        bloc (int): type de bloc
        donnees (int, optionnel): informations supplémentaires (couleur, type de bois...)
    """
    conn.send("world.setBlock", intFloor(
        coord[0], coord[1], coord[2], bloc, donnees))


def recuperer_altitude(coord: tuple) -> int:
    """
    Récupère l'altitude de coordonnées horizontales (x,z)

    Paramètres:
        coord (tuple): coordonnées du bloc

    Renvoi:
        int: hauteur maximale à ce point
    """
    return int(conn.sendReceive("world.getHeight", intFloor(coord[0], coord[2])))


def recuperer_id(nom: str) -> int:
    """
    Récupère l'identifiant du joueur selon son nom
    Lève une assertion si le nom est inconnu

    Paramètres:
        nom (str): nom du joueur

    Renvoi:
        int: id du joueur
    """
    id = conn.sendReceive("world.getPlayerId", nom)
    if id == "fail":
        print("Attention! Nom de joueur inconnu; valeur renvoyée: 0")
        return 0
    else:
        return int(id)


def recuperer_ids() -> list:
    """
    Récupère les identifiants de tous les joueurs

    Renvoi:
        list: tableau des identifiants
    """
    infos = conn.sendReceive("world.getPlayerIds")
    ids = map(int, infos.split("|"))
    return list(ids)


def sauvegarder() -> None:
    """
    Sauvegarde un point de contrôle qui peut être utilisé pour restaurer un état du jeu
    """
    conn.send("world.checkpoint.save")


def restaurer() -> None:
    """
    Restaure l'état du jeu au moment de la sauvegarde d'un point de contrôle
    """
    conn.send("world.checkpoint.restore")


def poster(msg: str) -> None:
    """
    Poste un message sur le chat

    Paramètres:
        msg (str): le message à poster
    """
    conn.send("chat.post", msg)

# Fonctions joueur


def recuperer_ma_position() -> tuple:
    """
    Récupère la position de la tuile sous le joueur

    Renvoi:
        tuple: coordonnées (x, y, z)
    """
    s = conn.sendReceive("entity.getTile", player)
    return tuple(map(int, s.split(",")))


def changer_ma_position(coord: tuple) -> None:
    """
    Repositionnement (absolu ou relatif) du joueur sur une autre tuile

    Paramètres:
        coord (tuple): nouvelle coordonnées
    """
    conn.send("entity.setTile", player, intFloor(coord[0], coord[1], coord[2]))


def recuperer_ma_rotation() -> float:
    """
    Récupère l'angle de rotation dans le plan horizontal du joueur 

    Renvoi:
        float: angle dans le plan Oxz (0° à 360°)
    """
    s = conn.sendReceive("entity.getRotation", player)
    return float(s)


def recuperer_mon_inclinaison() -> float:
    """
    Récupère l'angle de rotation dans le plan vertical du joueur 

    Renvoi:
        float: angle dans le plan Oxy (-90° à 90°)
    """
    s = conn.sendReceive("entity.getPitch", player)
    return float(s)


def recuperer_ma_direction() -> tuple:
    """
    Récupère le vecteur unitaire du cap du joueur

    Renvoi:
        tuple: coordonnées (x, y, z)
    """
    s = conn.sendReceive("entity.getDirection", player)
    return tuple(map(float, s.split(",")))

# Fonctions autres joueurs


def recuperer_position(id: int) -> tuple:
    """
    Récupère la position de la tuile sous le joueur 'id'

    Paramètres:
        id (int): identifiant du joueur

    Renvoi:
        tuple: coordonnées (x, y, z)
    """
    ids = recuperer_ids()
    if id in ids:
        s = conn.sendReceive("entity.getTile", id)
        return tuple(map(int, s.split(",")))
    else:
        print("Attention! Joueur inconnu, impossible de récupérer sa position; valeur renvoyée: (0, 0, 0)")
        return (0, 0, 0)


def changer_position(id: int, coord: tuple) -> None:
    """
    Repositionnement du joueur 'id' sur une autre tuile

    Paramètres:
        id (int): identifiant du joueur
        coord (tuple): nouvelle coordonnées
    """
    ids = recuperer_ids()
    if id in ids:
        conn.send("entity.setTile", id, intFloor(coord[0], coord[1], coord[2]))
    else:
        print("Attention! Joueur inconnu, impossible de le bouger")


def recuperer_rotation(id: int) -> float:
    """
    Récupère l'angle de rotation dans le plan horizontal du joueur 'id'

    Paramètres:
        id (int): identifiant du joueur

    Renvoi:
        float: angle dans le plan Oxz (0° à 360°)
    """
    ids = recuperer_ids()
    if id in ids:
        s = conn.sendReceive("entity.getRotation", id)
        return float(s)
    else:
        print("Attention! Joueur inconnu, impossible de récupérer sa rotation; valeur renvoyée: 0")
        return 0


def recuperer_inclinaison(id: int) -> float:
    """
    Récupère l'angle de rotation dans le plan vertical du joueur 'id'

    Paramètres:
        id (int): identifiant du joueur

    Renvoi:
        float: angle dans le plan Oxy (-90° à 90°)
    """
    ids = recuperer_ids()
    if id in ids:
        s = conn.sendReceive("entity.getPitch", id)
        return float(s)
    else:
        print("Attention! Joueur inconnu, impossible de récupérer son inclinaison; valeur renvoyée: 0")
        return 0


def recuperer_direction(id: int) -> tuple:
    """
    Récupère le vecteur unitaire du cap du joueur

    Paramètres:
        id (int): identifiant du joueur

    Renvoi:
        tuple: coordonnées (x, y, z)
    """
    ids = recuperer_ids()
    if id in ids:
        s = conn.sendReceive("entity.getDirection", id)
        return tuple(map(float, s.split(",")))
    else:
        print("Attention! Joueur inconnu, impossible de récupérer son inclinaison; valeur renvoyée: (0,0,0)")
        return (0, 0, 0)
