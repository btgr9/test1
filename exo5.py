
user_list = {}
while True:
    print("Quel profil avez vous 🤔")
    print("1- Nouveau profil")
    print("2- Profil existant")
    reponse1=int(input(""))
    if reponse1 == 1:
        nom_utilisateur=input(" Veuillez entrer votre nom s'il vous plait 😄 ")
        solde_actuel=int(input(f"Quel es votre solde actuel💰 "))
        user_list[nom_utilisateur] = solde_actuel
        code_pin=int(input("Definissez votre code pin💻 :"))
        print("Que souhaitez vous faire?🤔")
        print("1. Rechargez cotre compte")
        print("2. Envoyer de l'argent")
        print("3. retirer de l'argent")
        print("4. Consulter mon solde")
        reponse2 = int(input(""))
        if reponse2 == 1:
            ajout =int(input("Combien voulez vous ajouter au solde"))
        
            solde_actuel=solde_actuel + ajout
            print(f"Votre solde es de: {solde_actuel}")
            solde_actuel=solde_actuel+ajout
            print("Operation reussie avec succes✅")
            print(f"Votre solde est de: {solde_actuel}")

        if reponse2 == 2:
            envoi = int(input("Combien voulez vous envoyer"))
            print("Entrez votre mot de passe")
            login = int(input(""))
            if envoi<solde_actuel :
                if login == code_pin :
                    solde_actuel=solde_actuel - envoi
                    print(f"Votre solde es de: {solde_actuel}")
                else :
                    print("Code pin invalide ❌")
            
            else :
                print("Solde insuffisant😞")
        if reponse2 == 3:
            retrait = int(input("Combien voulez vous retirer du solde"))
            print("Entrez votre mot de passe")
            login = int(input(""))
            
            if retrait<solde_actuel:
                if login == code_pin :
                    solde_actuel=solde_actuel - retrait
                    print(f"Votre solde es de: {solde_actuel}")
                else :
                    print("Code pin invalide ❌")
                solde_actuel=solde_actuel-retrait
                print("Operation reussie avec succes✅")
                print(f"Votre solde es de: {solde_actuel}")
            else :
                print("Solde insuffisant😞")
        if reponse2 == 4:
            print(f"Votre solde actuel es de: {solde_actuel}")
        else:
            print("Choix invalide ❌")  
    if reponse1 == 2:
        nom_utilisateur=input(" Veuillez entrer votre nom s'il vous plait 😄 ")
        print(f"Bonjour {nom_utilisateur}🤗 ")
        if nom_utilisateur in user_list:
            for nom_utilisateur, solde_actuel in user_list.items(): 
                print(f" {nom_utilisateur} votre solde actuel es de : {solde_actuel}.")
        nom_utilisateur=input(" Veuillez entrer votre nom s'il vous plait 😄 ")
        solde_actuel=int(input(f"Quel es votre solde actuel💰 "))
        code_pin=int(input("Definissez votre code pin💻 :"))
        print("Que souhaitez vous faire?🤔")
        print("1. Rechargez cotre compte")
        print("2. Envoyer de l'argent")
        print("3. retirer de l'argent")
        print("4. Consulter mon solde")
        reponse2 = int(input(""))
        if reponse2 == 1:
            ajout =int(input("Combien voulez vous ajouter au solde"))
        
            solde_actuel=solde_actuel + ajout
            print(f"Votre solde es de: {solde_actuel}")
            solde_actuel=solde_actuel+ajout
            print("Operation reussie avec succes✅")
            print(f"Votre solde est de: {solde_actuel}")

        if reponse2 == 2:
            envoi = int(input("Combien voulez vous envoyer"))
            print("Entrez votre mot de passe")
            login = int(input(""))
            if envoi<solde_actuel :
                if login == code_pin :
                    solde_actuel=solde_actuel - envoi
                    print(f"Votre solde es de: {solde_actuel}")
                else :
                    print("Code pin invalide ❌")
            
            else :
                print("Solde insuffisant😞")
        if reponse2 == 3:
            retrait = int(input("Combien voulez vous retirer du solde"))
            print("Entrez votre mot de passe")
            login = int(input(""))
            
            if retrait<solde_actuel:
                if login == code_pin :
                    solde_actuel=solde_actuel - retrait
                    print(f"Votre solde es de: {solde_actuel}")
                else :
                    print("Code pin invalide ❌")
                solde_actuel=solde_actuel-retrait
                print("Operation reussie avec succes✅")
                print(f"Votre solde es de: {solde_actuel}")
            else :
                print("Solde insuffisant😞")
        if reponse2 == 4:
            print(f"Votre solde actuel es de: {solde_actuel}")
        else:
            print("Choix invalide ❌")  
    cmd = input("Tape 'q' pour quitter : ") 
    if cmd == "q": 
        break

        
        


    
    
    

    
