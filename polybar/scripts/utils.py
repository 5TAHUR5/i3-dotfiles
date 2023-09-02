import subprocess


class Utils():

    #   Получить координаты мыши
    def get_spawn_coordinates(window_w):
        mouse_coors = subprocess.Popen(["xdotool", "getmouselocation", "--shell"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).communicate()[0].split("\n")
        return (str(int(mouse_coors[0].split("=")[1]) - int(window_w) / 2).split(".")[0], mouse_coors[1].split("=")[1])
        #return (spawn_x, spawn_y)



