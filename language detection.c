#include <stdio.h>
#include <string.h>

int main() {
    char word[15];  // max length 14 + null terminator
    int case_num = 1;
    
    while (1) {
        scanf("%s", word);
        
        if (word[0] == '#') {
            break;
        }
        
        if (strcmp(word, "HELLO") == 0) {
            printf("Case %d: ENGLISH\n", case_num);
        }
        else if (strcmp(word, "HOLA") == 0) {
            printf("Case %d: SPANISH\n", case_num);
        }
        else if (strcmp(word, "HALLO") == 0) {
            printf("Case %d: GERMAN\n", case_num);
        }
        else if (strcmp(word, "BONJOUR") == 0) {
            printf("Case %d: FRENCH\n", case_num);
        }
        else if (strcmp(word, "CIAO") == 0) {
            printf("Case %d: ITALIAN\n", case_num);
        }
        else if (strcmp(word, "ZDRAVSTVUJTE") == 0) {
            printf("Case %d: RUSSIAN\n", case_num);
        }
        else {
            printf("Case %d: UNKNOWN\n", case_num);
        }
        
        case_num++;
    }
    
    return 0;
}
