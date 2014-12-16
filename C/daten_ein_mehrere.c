#include <stdio.h>

int main()
{
   int tag, monat, jahr, anzahl;

   /* Eingabe mit Standard-Trennzeichen */
   printf("Bitte geben Sie Tag, Monat und Jahr ein\n");
   printf("Trennung mit Leerzeichen, Tab oder Return:\n");
   anzahl = scanf("%d%d%d", &tag, &monat, &jahr);
   printf("Datum: %d.%d.%d\n", tag, monat, jahr);
   printf("Gelesen: %d\n\n", anzahl);

   /* Eingabe mit Formatangabe */
   printf("Bitte geben Sie Tag, Monat und Jahr ein\n");
   printf("in der Form T.M.J:\n");
   anzahl = scanf("%d.%d.%d", &tag, &monat, &jahr);
   printf("Datum: %d.%d.%d\n", tag, monat, jahr);
   printf("Gelesen: %d\n\n", anzahl);

   return 0;
}
