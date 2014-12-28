#include <stdio.h>

int main()
{
   /* Deklaration */
   int anzahl;
   double preis;

   /* Erste Eingabe */
   printf("Anzahl eingeben: ");
   scanf("%d", &anzahl);

   /* Zweite Eingabe */
   printf("Preis in Euro eingeben: ");
   scanf("%lf", &preis);

   /* Ausgabe */
   printf("Anzahl: %d\n", anzahl);
   printf("Preis: %.2f Euro\n", preis);

   return 0;
}
