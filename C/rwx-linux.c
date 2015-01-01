#include <stdio.h>
#include <sys/stat.h>
#include <time.h>

int main(int argc, char **argv)
{
   char vektor[10] = "---------";

   struct stat attr;
   if(stat(argv[1], &attr))
   {
      printf("Kein Zugriff auf Dateiattribute\n");
      return 1;
   }
	
   if(attr.st_mode & S_IFREG)      printf("Regulaere Datei\n");
   else if(attr.st_mode & S_IFDIR) printf("Verzeichnis\n");
	
   if(attr.st_mode & S_IRUSR) vektor[0] = 'r';
   if(attr.st_mode & S_IWUSR) vektor[1] = 'w';
   if(attr.st_mode & S_IXUSR) vektor[2] = 'x';
   if(attr.st_mode & S_IRGRP) vektor[3] = 'r';
   if(attr.st_mode & S_IWGRP) vektor[4] = 'w';
   if(attr.st_mode & S_IXGRP) vektor[5] = 'x';
   if(attr.st_mode & S_IROTH) vektor[6] = 'r';
   if(attr.st_mode & S_IWOTH) vektor[7] = 'w';
   if(attr.st_mode & S_IXOTH) vektor[8] = 'x';
   printf("%s Zugriffsrechte\n", vektor);

   printf("%d UID\n", attr.st_uid);
   printf("%d GID\n", attr.st_gid);
   printf("%lld Byte\n", attr.st_size);
   printf("Letzter Zugriff: %s", ctime(&attr.st_atime));
   printf("Letzte Aenderung: %s", ctime(&attr.st_mtime));
   printf("Letzte Aenderung Status: %s\n", ctime(&attr.st_ctime));

   return 0;
}
