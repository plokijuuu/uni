#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N 30
#define MAX 10
typedef struct osoba 
{
    char *imie;
    char *nazwisko;
    char *miejscowosc;
    int wiek;
} OSOBA;

void inicjalizacja_OSOBA(OSOBA *osoba, char *imie, char *nazwisko, char *miejscowosc, int wiek);
void wyswietl(OSOBA *osoba);
void dealokacja_OSOBA(OSOBA *osoba);

int main(void)
{
	OSOBA dane[MAX];
    char tab_imie[N + 1];
    char tab_nazwisko[N + 1];
    char tab_miejscowosc[N + 1];
    int i = 0, age, k;

    // Wprowadzanie danych do tablicy struktur
    while (i < MAX) {
        printf("Podaj imie: ");
        gets(tab_imie);

        printf("Podaj nazwisko: ");
        gets(tab_nazwisko);

        printf("Podaj miejscowosc: ");
        gets(tab_miejscowosc);

        printf("Podaj wiek: ");
        scanf("%d", &age);
        while (getchar() != '\n'); 

        // Inicjalizacja struktury
        inicjalizacja_OSOBA(&dane[i], tab_imie, tab_nazwisko, tab_miejscowosc, age);
        i++;
    }

    // Wyœwietlanie wybranych rekordów
    printf("Podaj, ktory rekord tablicy dane chcesz wyswietlic.\n");
    printf("Wyjscie poza indeks tablicy lub wpisanie znaku nie bedacego liczba konczy wypisywanie!\n");

    while (scanf("%d", &k) == 1 && k >= 0 && k < MAX) {
        printf("Rekord %d\n", k);
        printf("----------------------------------------\n");
        wyswietl(&dane[k]);
        printf("----------------------------------------\n");

        while (getchar() != '\n'); 
        printf("Podaj ktory rekord tablicy dane chcesz wyswietlic.\n");
        printf("Wyjscie poza indeks tablicy lub wpisanie znaku nie bedacego liczba konczy wypisywanie!\n");
    }
	int j;
    // Dealokacja pamiêci
    for (j = 0; j < MAX; j++) {
        dealokacja_OSOBA(&dane[j]);
    }

    printf("KONIEC!\n");
    return 0;
	return 0;
}

void inicjalizacja_OSOBA(OSOBA *osoba, char *imie, char *nazwisko, char *miejscowosc, int wiek) 
{
    // Alokacja pamiêci i kopiowanie imienia
    osoba->imie = (char *)malloc((strlen(imie) + 1) * sizeof(char));
    if (osoba->imie != NULL) 
	{
        strcpy(osoba->imie, imie);
    }

    // Alokacja pamiêci i kopiowanie nazwiska
    osoba->nazwisko = (char *)malloc((strlen(nazwisko) + 1) * sizeof(char));
    if (osoba->nazwisko != NULL) 
	{
        strcpy(osoba->nazwisko, nazwisko);
    }

    // Alokacja pamiêci i kopiowanie miejscowoœci
    osoba->miejscowosc = (char *)malloc((strlen(miejscowosc) + 1) * sizeof(char));
    if (osoba->miejscowosc != NULL) 
	{
        strcpy(osoba->miejscowosc, miejscowosc);
    }

    // Przypisanie wieku
    osoba->wiek = wiek;
}

void wyswietl(OSOBA *osoba) 
{
    printf("Imie: %s\n", osoba->imie);
    printf("Nazwisko: %s\n", osoba->nazwisko);
    printf("Miejscowosc: %s\n", osoba->miejscowosc);
    printf("Wiek: %d\n", osoba->wiek);
}

void dealokacja_OSOBA(OSOBA *osoba) 
{
    if (osoba->imie != NULL) 
	{
        free(osoba->imie);
        osoba->imie = NULL;
    }
    if (osoba->nazwisko != NULL) 
	{
        free(osoba->nazwisko);
        osoba->nazwisko = NULL;
    }
    if (osoba->miejscowosc != NULL) 
	{
        free(osoba->miejscowosc);
        osoba->miejscowosc = NULL;
    }
}

