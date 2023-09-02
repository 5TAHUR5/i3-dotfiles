

#####   STATE settings   ######
class State_Settings():
    second_for_update = 2                             #Частота обновления
    window_w = "250"                                  #Ширина окна
    def sigh_label_text(insert_text):                 #Строка сверху     
        return f"PID  | %{insert_text}  | COMMAND"          
    font_for_lbl = ("Iosevka", 10)                    #Используемый шрифт
    count_pid = 5                                     #Количество отображаемых процессов


#####   FILESYSTEM settings   ######
class Filesystem_Settings():
    font_btn_text = ("Iosevka", 10) 
    window_w = "250"                                  #Ширина окна
    file_manager = "thunar"
    directories = []
    directories.append(".config")
    directories.append("Загрузки")
    #directories.append("")
    #directories.append("")
    #directories.append("")
    #directories.append("")

    






