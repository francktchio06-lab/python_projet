#include <iostream>
#include <string>
using namespace std;

// Fonction pour chiffrer ou déchiffrer un message avec le chiffre de César
string cesar(string message, int decalage) {
    string resultat = "";
    for (char lettre : message) {
        if (isalpha(lettre)) {
            char base = isupper(lettre) ? 'A' : 'a';
            char lettre_chiffree = (lettre - base + decalage) % 26 + base;
            resultat += lettre_chiffree;
        } else {
            resultat += lettre; // Conserve les caractères non alphabétiques
        }
    }
    return resultat;
}

int main() {
    string message_original = "HELLO WORLD"; // Votre message ici
    int decalage = 3; // Le décalage (clé) pour le chiffrement

    // Chiffrer le message
    string message_chiffre = cesar(message_original, decalage);
    cout << "Message chiffré : " << message_chiffre << endl;

    // Déchiffrer le message
    string message_dechiffre = cesar(message_chiffre, -decalage);
    cout << "Message déchiffré : " << message_dechiffre << endl;

    return 0;
}
