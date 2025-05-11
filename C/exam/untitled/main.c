#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Task1
struct Medicine {
    char name[31];
    char date[8];
    long long id;
    float price;
    int quantity;
};

typedef struct Medicine Medicine;

//Task2
int convertMonth(char date[]) {
    int month = (date[0] - '0') * 10 + (date[1] - '0');
    return month;
}

int convertYear(char date[]) {
    int year = (date[3] - '0') * 1000 + (date[4] - '0') * 100 +(date[5] - '0') * 10 + (date[6] - '0');
    return year;
}

Medicine* filterByExpiry(Medicine medicines[], int count, char checkDate[],int *checker) {
        *checker = 0;
        Medicine* filtered_medicine = (Medicine*)malloc(count * sizeof(Medicine));
        if (filtered_medicine == NULL) {
            printf("Memory allocation error");
            return NULL;
        }

        for (int i = 0; i < count; i++) {
            if (convertYear(medicines[i].date) < convertYear(checkDate) || (convertYear(medicines[i].date) == convertYear(checkDate) && convertMonth(medicines[i].date) < convertMonth(checkDate))) {
                filtered_medicine[*checker] = medicines[i];
                *checker++;
            }
        }
        if (checker == 0) {
            free(filtered_medicine);
            return NULL;
        }
        return filtered_medicine;
}

//Task3
int saveOffersInFile(Medicine* medicines, int count, float min_price, float max_price) {
    int offers = 0;
    FILE *file;
    file = fopen("offers.txt", "w");
    if (file == NULL) {
        printf("File could not be opened");
        return -1;
    }

    for (int i = 0; i < count; i++) {
        if (min_price <= medicines[i].price && medicines[i].price <= max_price) {
            offers++;
            fprintf(file,"%s \n%s \n%lld \n%fleva",medicines[i].name, medicines[i].date, medicines[i].id, medicines[i].price);
        }
    }

    fclose(file);
    return offers;
}

//Task4
void deleteMedicine(Medicine* medicines, int* count, char name[], char date[]) {
    int checker = 0;
    Medicine* new_medicines;

    for (int i = 0; i < *count; i++) {
        if (strcmp(medicines[i].name, name) == 0 && convertYear(medicines[i].date) == convertYear(date) && convertMonth(medicines[i].date) == convertMonth(date)) {
            checker++;
            medicines[i].name = {"NULL"};
        }
    }
    if (checker == 0) {
        printf("There is no such medicine");
    }
    else {
        *count -= checker;
        new_medicines = (Medicine*)malloc(*count * sizeof(Medicine));
        if (new_medicines == NULL) {
            printf("Memory allocation error");
            return;
        }

        for (int i = 0 ; i < *count; i++) {
            int j = 0;
            if (medicines[i].name != "NULL") {
                new_medicines[j] = medicines[i];
                j++;
            }
        }
        medicines = new_medicines;
        free(new_medicines);
        printf("Medicine with name %s and date %s has been deleted", name, date);
    }
}


int main(void) {
    int capacity = 10;
    int count = 0;
    Medicine currentMedicine;
    Medicine *medicines;
    int ex = 0;

    //Task1
    FILE *bfile = fopen("medicines.bin", "rb");
    if (bfile == NULL) {
        printf("File could not be opened");
        return 1;
    }

    printf("File opened successfully");

    medicines = (Medicine*)malloc(sizeof(Medicine) * capacity);
    if (medicines == NULL){
        printf("Memory could not be allocated");
        fclose(bfile);
        return 1;
    }

    while(fread(&currentMedicine, sizeof(Medicine), 1, bfile)) {
        if (count >= capacity) {
            capacity *= 2;
            Medicine * newmedicines = (Medicine*)realloc(medicines, capacity * sizeof(Medicine));
            if (newmedicines == NULL) {
                printf("Memory could not be allocated");
                free(medicines);
                fclose(bfile);
                return 1;
            }

            medicines = newmedicines;
            free(newmedicines);
        }
        medicines[count] = currentMedicine;
        count++;
    }

    fclose(bfile);

    for (int i = 0; i < count; i++) {
        printf("Medicine[%d]: %s, Exp:%s, ID:%lld, %f lv {%d} \n", i, medicines[i].name, medicines[i].date, medicines[i].id, medicines[i].price, medicines[i].quantity);
    }

    //Task2
    Medicine* soonExpiring = filterByExpiry(&medicines, count, "07.2025", &ex);
    if (soonExpiring) {
        for (int i = 0; i < ex; i++) {
            printf("Medicine[%d]: %s, Exp:%s, ID:%lld, %f lv {%d} \n", i, soonExpiring[i].name, soonExpiring[i].date, soonExpiring[i].id, soonExpiring[i].price, soonExpiring[i].quantity);
        }
        free(soonExpiring);
    }
    else {
        printf("No medicines expiring before given date.\n");
    }

    //Task3
    printf("%d medicines saved to offer.txt.\n", saveOffersInFile(&medicines, count, 5.0, 15.0));

    //Task4
    deleteMedicine(&medicines,&count,"Aspirin","07.2025");

    free(medicines);
    return 0;
}