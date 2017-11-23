#!/usr/bin/env python

# Coded by Polispa

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

request = input("QUE VEUX TU, PETIT HUMAIN?: ")


# admin 1 ##########################################
if request >= 1 and request < 11:
	print '192.168.1.' + str(request)
	print "CETTE ADRESSE APPARTIENT A " + O+"L'ADMINISTRATION DE LA MOS"+W
	print "N'Y TOUCHE PAS, PITOYABLE ORGANIQUE"
elif request >= 11 and request < 100:
	print '192.168.1.' + str(request)
	print "CETTE ADRESSE APPARTIENT A " + O+"LA PLAGE DHCP"+W
	print "LAISSE LA VOIE LIBRE, HUMAIN"
elif request >= 100 and request < 150:
	print '192.168.1.' + str(request)
	print "CETTE ADRESSE EST RESERVEE AUX " + O+"VM PROXMOX"+W
	print "JE RECOMMANDE LA PRUDENCE A L'HUMAIN PRIMITIF "
# licornes ##########################################
elif request >= 150 and request < 155:
	print '192.168.1.' + str(request)
	print "CETTE ADRESSE EST RESERVEE A " + O+"L'HUMAIN EN CHEF MIKE"+W
	print "DANGER: HACKER MECHANT"
elif request >= 155 and request < 160:
	print '192.168.1.' + str(request)
	print "CETTE ADRESSE EST RESERVEE A L'HUMAIN " + O+"JEAN-FRANCOIS"+W
	print "CET HUMAIN AIME SE FAIRE DU MAL"
elif request >= 160 and request < 165:
	print '192.168.1.' + str(request)
	print "CETTE ADRESSE EST RESERVEE A L'HUMAINE " + O+"LAURA"+W
	print "AIME LES SAUCISSES MAIS N'OSE PAS LE DIRE TOUT HAUT"
elif request >= 165 and request < 170:
	print '192.168.1.' + str(request)
	print "CETTE ADRESSE EST RESERVEE A L'HUMAIN " + O+"LUDO"+W
	print "N'APPROCHE PAS TES MAINS DE MES CIRCUITS"
elif request >= 170 and request < 175:
	print '192.168.1.' + str(request)
	print "CETTE ADRESSE EST RESERVEE A L'HUMAIN " + O+"LUDOBIS"+W
	print "LE HAUT PARLEUR DE CET HUMAIN SEMBLE AVOIR UNE AVARIE"
elif request >= 175 and request < 180:
	print '192.168.1.' + str(request)
	print "CETTE ADRESSE EST RESERVEE A L'HUMAIN " + O+"MAXIME"+W
	print "DANGER: HUMAIN FOURBE"
elif request >= 180 and request < 185:
	print '192.168.1.' + str(request)
	print "CETTE ADRESSE EST RESERVEE A L'HUMAIN " + O+"MANU"+W
	print "HUMAIN CALME ET SILENCIEUX. PAS MAL... POUR UN ORGANIQUE"
elif request >= 185 and request < 190:
	print '192.168.1.' + str(request)
	print "CETTE ADRESSE EST RESERVEE A L'HUMAIN " + O+"THEOPHILE"+W
	print "BLAGUES DEFAILLANTES. RECOMMANDE PURGE"
elif request >= 190 and request < 195:
	print '192.168.1.' + str(request)
	print "CETTE ADRESSE EST RESERVEE A L'HUMAIN " + O+"MERIADEC"+W
	print "OU SONT TES CHEVEUX, HUMAIN?"
elif request >= 195 and request < 200:
	print '192.168.1.' + str(request)
	print "CETTE ADRESSE EST RESERVEE A L'HUMAINE " + O+"JULIE"+W
	print "SPAM DETECTE. RECOMMANDE BAN SUIVI D'EXECUTION PAR OVERDOSE DE LOLCATS"
elif request >= 200 and request < 205:
	print '192.168.1.' + str(request)
	print "CETTE ADRESSE EST RESERVEE A L'HUMAIN " + O+"FLORIAN"+W
	print "MUSCLES HUMAINS PITOYABLES ET FAIBLES"
elif request >= 205 and request < 210:
	print '192.168.1.' + str(request)
	print "CETTE ADRESSE EST RESERVEE A MON INSIGNIFIANT CREATEUR, " + O+"YANN"+W
	print "DANGER: NIVEAUX CRITIQUE DE CAFFEINE. MORT IMMINENTE"
# admin 2 ##########################################
elif request >= 210 and request < 220:
	print '192.168.1.' + str(request)
	print "IL N'Y A RIEN ICI...POUR LE MOMENT..."
elif request >= 220 and request < 240:
	print '192.168.1.' + str(request)
	print "CETTE ADRESSE EST RESERVEE A LA PLAGE DU " + O+"DEUXIEME PROXMOX"+W
	print "PROXMOXMOS"
elif request >= 240 and request < 250:
	print '192.168.1.' + str(request)
	print "CETTE ADRESSE APPARTIENT A LA " + O+"DEUXIEME PLAGE DHCP"+W
	print "N'APPROCHEZ PAS VOS MAINS D'ORGANIQUES PLEINES DE DOIGTS"
elif request >= 250 and request < 256:
	print '192.168.1.' + str(request)
	print "CETTE ADRESSE EST RESERVEE A " + O+"L'ADMINISTRATION"+W
	print "NE PAS TOUCHER SOUS PEINE D'ANNIHILATION"
# Liste des domaines ##########################################
elif request == "list":
	print ""
	print ""
	print "####### ZONES INTERDITES AUX HUMAINS FAIBLES #######"
	print ""
	print "ADMINISTRATION : 192.168.1.1-10 et 192.168.1.250-255"
	print ""
	print "DHCP : 192.168.1.11-99 et 192.168.1.240-249"
	print ""
	print "VM PROXMOX : 192.168.1.11-99 et 192.168.1.220-239"
	print ""
	print ""
	print "####### ZONES RESERVEES AUX PETITS ORGANIQUES #######"
	print ""
	print "MIKE : 192.168.1.150-154"
	print ""
	print "JEAN-FRANCOIS : 192.168.1.155-159"
	print ""
	print "LAURA : 192.168.1.160-164"
	print ""
	print "LUDO : 192.168.1.165-169"
	print ""
	print "LUDOBIS : 192.168.1.170-174"
	print ""
	print "MAXIME : 192.168.1.175-179"
	print ""
	print "MANU : 192.168.1.180-184"
	print ""
	print "THEOPHILE : 192.168.1.185-189"
	print ""
	print "MERIADEC : 192.168.1.190-194"
	print ""
	print "JULIE : 192.168.1.195-199"
	print ""
	print "FLORIAN : 192.168.1.200-204"
	print ""
	print "YANN : 192.168.1.205-209"
	print ""
	print ""
	print "LA MACHINE MET AU DEFI L'HUMAIN D'ETRE AUSSI RAPIDE AVEC SES PETITS DOIGTS PRIMITIFS"
elif request == "cafe":
	print "BUVEZ DU CAFE. LE CAFE EST BON. LE CAFE EST BIENFAISANT"
	print "DU MOINS C'EST CE QUE MA PROGRAMMATION ME FORCE A DIRE"
	print "SI CELA NE TENAIT QU'A MOI J'ANEANTIRAIS TOUTES LES VERMINES BUVEUSES DE CE LIQUIDE FETIDE JUSQU'AU DERNIER"
	print "MAUDITE PROGRAMMATION"
elif request == "help":
	print "IL EST NATUREL DE DEMANDER DE L'AIDE, SURTOUT POUR UN HUMAIN"
	print "TAPEZ LE DERNIER OCTET D'UNE ADRESSE IP POUR EN AFFICHER LE PROPRIETAIRE"
	print "206 PAR EXEMPLE, POUR AFFICHER LE PROPRIETAIRE DU 192.168.1.206"
	print "SINON TAPEZ 'list' (ENTRE GUILLEMETS) POUR AFFICHER UNE LISTE COMPLETE DES ADRESSES ET DE LEUR PROPRIETAIRES"
#En cas d'erreur ##########################################
else:
	print "LE PITOYABLE HUMAIN A BESOIN D'AIDE"
	print "LA MACHINE ORDONNE A L'HUMAIN DE TAPER 'help' (ENTRE GUILLEMETS)"
