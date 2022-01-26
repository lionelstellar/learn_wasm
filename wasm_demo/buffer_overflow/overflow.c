#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
int main()
{
    char log_success_msg[24] = "someone_login_success";
    char log_failed_msg[24] = "someone_login_failed";   
    char username[8] = {};
    char file_path[16] = "log/login.log";
    char password[8] = {};

    /* 输入账户、口令 */
    printf("input username and password:\n");
    scanf("%s", username);                              // username边界未检查，可能存在缓冲区溢出
    scanf("%s", password);                              // password边界未检查，可能存在缓冲区溢出

    /* 比较账户、口令是否正确 */
    char buf[1024] = {};
    if(!strcmp(username, "jack") && !strcmp(password, "123456")) {
        strcat(buf, log_success_msg);
        printf("login success!\n"); 
    } else {      
        strcat(buf, log_failed_msg);
        /* 登陆失败写入日志 */
        printf("[*] write %s to %s!\n", buf, file_path);
        int out = open(file_path, O_WRONLY | O_CREAT | O_APPEND, 0660);
        if (out < 0) {
            fprintf(stderr, "error opening output %s: %s\n", file_path, strerror(errno));
            exit(1);
        }
        write(out, buf, strlen(buf));
        write(out, "\n", 1);
    }
    return 0;
}
