
init -1000 python:
    
    import os.path
    
    def Img(file):
        if os.path.isfile("../../storage/images/%d/%s.png" % (1080,file)):
            return "../../storage/images/%d/%s.png" % (1080,file)
        else:
            return "../../storage/images/%d/%s.jpg" % (1080,file)
    
    def get_image(file):
        return "../../storage/images/%s" % file

init -100 python:
    
    store.selected_slot = "_"
    persistent._file_page = 1


init:

    transform center:
        xalign 0.5
        xanchor 0.5
        yanchor 0.0

    transform left:
        xalign 0.28
        xanchor 0.5
        yanchor 0.0

    transform right:
        xalign 0.72
        xanchor 0.5
        yanchor 0.0

    transform fleft:
        xalign 0.16
        xanchor 0.5
        yanchor 0.0

    transform fright:
        xalign 0.84
        xanchor 0.5
        yanchor 0.0

    transform cleft:
        xalign 0.355
        xanchor 0.5
        yanchor 0.0

    transform cright:
        xalign 0.645
        xanchor 0.5
        yanchor 0.0

    transform running_left:
        easeout 0.75 xpos -0.5

    transform running_left_back:
        xpos -0.5
        linear 0.75 xpos 0.05





init -1001 python:
    
    renpy.music.register_channel("sound", "sfx", False)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("sound3", "sfx", False)
    renpy.music.register_channel("sound_loop", "voice", True)
    renpy.music.register_channel("sound_loop2", "voice", True)
    renpy.music.register_channel("sound_loop3", "voice", True)
    renpy.music.register_channel("ambience", "voice", True)
    
    def volume(vol, chnl):
        renpy.music.set_volume(vol, channel=chnl)
    
    def stop_music():
        for chnl in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "music"):
            renpy.music.stop(channel=chnl)
