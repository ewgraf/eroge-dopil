init:
    screen central_text(s, size=32):
         text s xalign 0.5 yalign 0.5 size size
         
    image bg ext_road_sepia = im.Sepia("../../storage/images/bg/ext_road_day.jpg")
        
init 410 python:
    prologue = 0
    style.prologue_message = style.thoughts_day
    style.prologue_message.color = "#fff"
    style.prologue_message.size = 38
    style.prologue_message.xmaximum = 1570
    text_images = []
    def show_slowtext(text, n, padding=None, style = style.prologue_message):
        if padding==None:
            padding = 20*n
        if n not in text_images:
            text_images.append(n)
        renpy.show('text'+str(n), what = Text(text, slow=True, style=style, xpos=175, xanchor=0.0, yanchor=0.5, ypos=540+padding))
        renpy.with_statement(None)
        renpy.pause()
    def hide_slowtext(n):
        if n in text_images:
            del text_images[n]
            renpy.hide('text'+str(n))
    def clear_slowtext():
        for n in text_images:
            #del text_images[n]
            renpy.hide('text'+str(n))

label ii_eroge__prologue:
label ii_eroge_prologue:
    $ th_prefix = "«"
    $ th_suffix = "»"
 
    scene black
    play music music_memories_piano_outdoors fadein 3
    show screen central_text("Пролог")
    $ renpy.pause(99, hard=False)
    hide screen central_text
    
    scene bg ext_road_sepia 
    with dissolve
    $ renpy.pause(3, hard=False)
    
    #TODO - весь первый отрывок до "Аноним" стоит подать без nvl режима, просто по центру экрана, с сохранением написанных до этого строчек и очищением экрана от этих строчкой. Проще говоря, нвл без фона-подкладки.    
    # Done. Это текст в виде изображения + пара костылей
    $ show_slowtext("Если бы меня спросили о самом интересном событии в жизни, то я бы промолчал.", -1)
    $ show_slowtext("Я всегда относился к числу тех скучных людей, которым нечего рассказать о себе.", 1)
    $ clear_slowtext()
    $ show_slowtext("Немногие знакомые и родственники, считавшие своё мнение очень важным, не упускали момента поучать меня.", -8)
    $ show_slowtext("«Перед тобой открыты все дороги», - говорили они.", -5)
    $ show_slowtext("«Все ушли вперёд, а ты не сделал ни шагу с места», - говорили они.", -3)
    $ show_slowtext("И хотя я делал вид, что меня это не сильно заботит, в глубине души я чувствовал себя уязвлённым.", 0)
    $ show_slowtext("Тогда я не мог припомнить ничего из своего скудного жизненного опыта, за что себя хвалить, за что гордиться собой.", 4)
    $ show_slowtext("До какого-то времени это было правдой, но однажды всё изменилось.", 7)
    $ clear_slowtext()
    #TODO - перенести следующее предложение на чёрный фон по центру, подать с паузой и выключением трека.
    scene black with dissolve
    stop music fadeout 2
    $ renpy.pause(1, hard=True)
    # Done
    $ show_slowtext("Эта удивительная летняя история началась в морозный декабрьский вечер...", 0)
    $ clear_slowtext()
    $ renpy.pause(3, hard=True)
    
    play music music_no_tresspassing fadein 1
    scene anim prologue_monitor_4 with dissolve
    $ renpy.pause(1, hard=True)

    $ set_mode_nvl()
    window show
    "\n\nАноним Пн 25 декабря 2009 16:30:26 №1004195
    \n\nАнонимус! Два года назад миру явилось чудо: невинная история о том, как одинокий паренёк встретил неку. Неважно, правда это или вымысел, но легенда отразила в себе понятную нам всем мечту о простом человеческом тепле, которого не хватает сетевым завсегдатаям. Судьбоносная встреча произошла в Москве в суетливый предновогодний день в самом обычном на первый взгляд месте - в Макдональдсе...
    Говорят, волшебную девочку-кошку  можно встретить в этот день, а именно - 29 декабря. Не упусти свой шанс, анонимус!"
    "\n\nИ вторым постом: «Это надо отметить 29-ого. Выпьем колы за здоровье неки. Алсо, нужна программа на вечер»." 
    "В десятке последующих сообщений посетители форума выясняли, как организовать по этому случаю встречу в Макдональдсе на Пушкинской. Основной протест у некоторых участников дискуссии вызывала сама идея сходки, куда неизбежно подтянутся люди из соцсетей, далёкие от духа и буквы имиджборды..."
    "Всё бы ничего, если бы не один пост случайного анонимуса." 
    "Мимо такой претензии на истину скептики не могли пройти."
    nvl clear
    "\n\n\n\n\n\nАноним Пн 25 декабря 2009 17:00:08 №1004221
    \n\n> Неважно, правда это или вымысел
    \n\nКак это неважно? Это всё было взаправду."
    "\n\nАноним Пн 25 декабря 2009 17:00:41 №1004222
    \n\nАвтор истории, это ты?"
    nvl clear
    "Тред быстро стал дырявым: часть сообщений в разгоревшемся споре оперативно удалялась модератором. Уже было всё равно, чья сторона одержит верх, в каждом лагере спорщиков о правдивости легенды насчитывались жертвы банхаммера."
    "За феерическим разгромом последовало осторожное сообщение:"
    "\nАноним Пн 25 декабря 2009 17:38:08 №1004276
    \n\nЭм, господа... Пожалуй, я пересоздам тред позже.
    \n\n{i}ОП{/i}"
    "\n\nА через минуту тред был удалён."
    "Везде и навсегда."
    "Ни веб-кэши, ни арихивы имиджборд не сохранили дискуссию от начала до конца, движок форума не учёл нумерацию постов, как если бы их не написали. Даже сделанные несколькими анонимами скриншоты таинственным образом к ночи обернулись повреждёнными файлами, которые невозможно было ни открыть какой-либо программой, ни восстановить."
    "Анонимы, желавшие напомнить о былинном споре, будто забывали о наболевшем и создавали новые треды и посты на совершенно другие, отвлечённые темы, вроде «Эй, анон, а давай будем делать свои почтовые марки?» и переписывания стихов Маяковского."
    nvl clear
    "\n\n\n\n\n\nСловом, тот тред был стёрт с лица Земли."
    stop music fadeout 2
    nvl clear
    window hide
    scene black
    with dissolve
    $ renpy.pause(3, hard=True)
    $ set_mode_adv()
    play music music_list["drown"] fadein 3 
    scene anim prolog_1
    with fade
    "Я помню каждое своё пробуждение."
    scene anim prolog_2
    with dissolve
    "Помню так отчётливо, как если бы оно было вырезано у меня в зрачках или на обратной стороне век."
    scene anim prolog_3
    with fade
    "Даже сейчас, не открывая глаз, я вижу все тот же нависающий надо мной потолок, который не стал за ночь ни выше, ни ниже."
    "Не стал другим."
    "И который, конечно же, никуда не исчез."
    scene anim prolog_4
    with dissolve
    "Я помню каждое своё пробуждение — просто потому, что каждый день всю мою жизнь начинался одинаково."
    "Радость сна уходила, оставляя меня наедине с реальностью, и открытые глаза не делали эту жизнь понятнее."
    scene anim prolog_5
    with dissolve
    "Все куда-то уходили. {w=.4}Всегда."
    "А я оставался. {w=.4} Всегда."
    "Оставался в пустой квартире, чем-то занимался и даже не запоминал — чем."
    "Потому что сами дни не отличались друг от друга."
    "Так же, как и одинаковое утро, они были лишь квинтэссенцией дня."
    "В конце концов они все слились воедино."
    "Слились в один день, когда я уже не мог сказать, что было в прошлый четверг, а что — два года назад."
    "Я словно попал в безвременье, где ничто не имело значения."
    "Дни текли, и не было ничего, что придавало бы этому течению смысл."
    scene anim prolog_10
    with dissolve
    "Раньше, когда я ещё учился, были обязанности."
    "Ходить на учёбу, слушать и запоминать сухие лекции, сдавать экзамены."
    "Но это быстро ушло."
    "Я бросил университет на втором же курсе."
    scene anim prolog_11
    with dissolve
    "Почему? {w=.4}Не знаю."
    "Наверное, я просто не выдержал того, что люди вокруг меня неслись в круговороте жизни, а я..."
    "Я оставался прежним. И никак не мог измениться."
    "Учёба ушла в небытие."
    "Когда это произошло — шесть лет назад? Это уже не имело значения."
    "Теперь я оставался дома."
    "Какие-то редкие попытки работать давали возможность существовать, но не более."
    "Мать изредка звонила мне, пытаясь ободрить, но..."
    "В конце концов вся работа прекращалась, и я вновь оставался в пустой квартире."
    "Я оставался один. {w=.4} Всегда."
    stop music fadeout 2
    # Blink?
    show blink
    "..."
    "......"
    "........."
    window hide
    play sound_loop sfx_home_phone_ring fadein 1
    scene anim prologue_keyboard_monitor_3
    with dissolve
    window show
    hide blink
    "Из дрёмы меня вывел телефонный звонок."
    "На этот раз я проснулся не в постели, а в кресле перед включённым компьютером."
    "Видимо, настолько утомился от безвылазного просиживания штанов, что даже не заметил, как уснул."
    "Я не сразу поднял трубку телефона — сначала надел очки."
    window hide
    scene anim prologue_keyboard_monitor_4
    with dissolve
    $ renpy.pause(2, hard=True)
    scene bg semen_room
    with dissolve
    stop sound_loop
    play music music_list["my_daily_life"] fadein 1
    window show
    "Звонила мама.{w} Она в очередной раз интересовалась моими делами и планами на будущее. Надеялась услышать хорошие новости — изменилось ли хоть что-то в моей жизни? Но я лишь произносил дежурные отговорки." 
    "Пока я говорил с матерью, параллельно вывел компьютер из спящего режима и посмотрел на время.{w} Четверть восьмого."
    "Прибраться в комнате? У меня всё чисто.{w} Разве что надо вынести мусор и пластиковые бутылки. Я ничего не сказал о смятых упаковках еды, разбросанной одежде и даже об окурке сигареты на полу."
    "Если что-то не надо выбрасывать, то оно на своём месте, а где лежит — неважно."
    "Отклеившуюся полосу обоев я не удосужился вернуть на место или заменить — было лень нести стул из кухни или разбирать тумбочку, на которой взгромоздился системный блок компьютера."
    "Работа? Какая работа может быть, если на носу праздничная неделя?{w} С деньгами пока всё в порядке, в последние годы я уже привык жить на часть маминой зарплаты и больше не испытывал угрызений совести, когда просил мать выделить немного денег на еду."
    "Я сказал, что если не буду занят, то навещу её перед Новым Годом - отметить праздник в семейном кругу.{w} В неполном семейном кругу — мои родители развелись в аккурат после того, как я бросил институт."
    "Я не стал выдумывать, чем буду занят в новогоднюю ночь, да и это было не нужно, главное убедить, что нет никаких проблем. На том я обычно заканчивал разговор."
    "После обмена прощаниями я положил трубку и откинулся на спинку кресла." 
    "Одиночество не проблема, в отличие от подлого чувства, что время уходит в никуда." 
    "Как я буду вспоминать о молодости через тридцать лет?{w} С сожалением?{w} Я старался не задумываться о таких вещах.{w} Лучше найти себе занятие на вечер, например, посмотреть кино или почитать что-нибудь интересное."
    "Близилось время ужина, и я понял, что совсем забыл о еде."
    "Подождав минуту, я встал с кресла и проверил содержимое холодильника у кровати." 
    "На полках ничего нет. Минералка и кола закончились, опустошённые пластиковые бутылки были расставлены по комнате, а одну из них, упавшую на пол, я не подобрал."
    th "Надо будет выбросить их."
    "На кухне ситуация была не лучше. На дверце висела прикреплённая магнитиком записка, сделанная мной утром."
    "{i}«Сходить за продуктами. Обязательно».{/i}"
    "Последнее слово подчёркнуто."
    th "Ну, раз {u}обязательно{/u}, то..."
    "В раздумьях я коснулся жёсткой щетины на лице."
    "Желание готовить ужин отсутствовало."
    "Если выберусь на улицу, хоть подышу свежим воздухом. Один из немногих поводов уходить на время из квартиры."
    "Лень заниматься готовкой заставила меня вспомнить о сетях быстрого питания."
    th "Можно сходить в Макдональдс у метро. По деньгам выйдет примерно столько же, как на покупку всех нужных продуктов."
    "Я вернулся в комнату со смятой запиской, которая тут же была запущена в мусорный пакет."
    th "Не попал."
    #stop music fadeout 2 # Перенести позже?
    "Одеваясь, я попутно развернул второе окно браузера с тредом форума, где обсуждали историю про анонима, встретившего девочку-кошку в Макдональдсе."
    th "А ведь я уснул как раз при чтении треда, когда свернул окно."
    "Последнее прочитанное мной сообщение принадлежало кому-то из спорщиков, полагавших, что образ девочки-кошки не играет роли, суть истории не в её необычной внешности."
    "Я же разделял мнение, что легенда остаётся всего лишь добрым вымыслом, а сходка в Макдональдсе в некотором смысле разрушает интимность рассказа. Заснув, я даже не поучаствовал в дискуссии, а мог бы высказаться."
    stop music fadeout 2
    "Подстёгиваемый любопытством, я обновил страницу и..."
    "В адресной строке значилось «about:blank», что противоречило всем моим ожиданиям."
    th "Такого не бывает!" # Shake?
    "Проверка истории браузера и кэша ничего не дала. Оставалось только развести руками и выключить компьютер. Разбираться в этой загадке у меня не было времени."
    "Распихав по карманам ключи, мобильник, кошелёк и сложенные очки, я покинул квартиру." # Music start
    "Я не горел желанием проверять правдивость легенды, ведь с большой вероятностью 29 декабря встреча состоится, а общаться с кем-то вживую мне хотелось меньше всего. Разве можно подумать, что там появится реальная девочка с кошачьими ушами?"
    "Не то чтобы я верил в сказки...{w} Я просто собирался поесть в Макдональдсе, который находится совсем не там, как требует легенда, и совсем не в то время." # Music fadeout
    ## Алсо, к: Макдак на Пушкинской является каноничным для сходочек, а вовсе не для истории. То было, емнип, у ВДНХ
    play ambience ambience_cold_wind_loop fadein 3
 
    window hide
 
    play sound sfx_intro_bus_stop_steps
 
    scene anim intro_1
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_2
    with dissolve
    $ renpy.pause(3, hard=True)
    scene anim intro_3
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_4
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_5
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_6
    with dissolve
    $ renpy.pause(3, hard=True)
    scene anim intro_7
    with fade
    $ renpy.pause(2, hard=True)
    scene bg bus_stop
    with dissolve
        
    $ renpy.pause(3)
    play music music_list["farewell_to_the_past_edit"] fadein 1
    window show
    "Пожалуй, единственным, что ещё окрашивало мою жизнь в какие-то полутона, были прогулки."
    "Я мог выходить только по вечерам."
    "Потому что днем потоки людей ещё тягуче струились по улицам."
    "Они сталкивались. Извиняясь или рыча вслед."
    "Извивались, чтобы обойти другой поток, и неслись дальше."
    "Вынести этого я уже не мог."
    "И только вечер успокаивал."
    "Люди расходились по домам, а я, словно в сумасшедшем желании отличиться от них, наоборот, выходил."
    "На остановке никого не было.{w} Ледяной ветер пронизывал дешёвое пальто, поэтому я спрятался от него под навесом."
    "Снегопад закончился, и я остался один на один с декабрьским холодом."
    "Автобус запаздывал, а идти пешком не хотелось — навстречу бы спешили люди, которые только что закончили работать и возвращались домой в спальные районы."
    "Мало-помалу я пришёл к пониманию, что зима — не лучшее время года, хотя длительность тёмного времени суток меня более чем устраивала. Можно дольше сидеть перед монитором, не прикрывая глаза от солнечного света."
    "Остальные плюсы и минусы казались несущественными."
    "Переминаясь с ноги на ногу по скрипящему снегу, я закрыл глаза в детской надежде согреться." # Blink
    "Яркое солнце, шелест листвы. Вокруг бегают дети.{w} Мои друзья. Смех, слезы, обида. Всё такое настоящее."
    "Мечты, надежды, цели. Я не хотел стать космонавтом, но я ни на секунду не сомневался, что стану важным.{w} Стану нужным."
    "Стану умным.{w} Красивым.{w} Встречу умницу-красавицу, которая полюбит меня с первого взгляда.{w} Я для неё, она для меня."
    "Я загадывал такие желания каждый день рожденья, когда задувал свечки."
    "Надо ли говорить, что ничего не сбылось?{w} Вспоминать об этом было горько."
    stop music fadeout 2
    window hide
    #TODO - поработать над всеми звуками для автобуса.
    # Да тот же набор скорости/остановка.
    play sound sfx_intro_bus_stop_sigh
    play sound_loop sfx_intro_bus_engine_loop fadein 1
    $ set_mode_adv()
    scene anim intro_9
    with fade2
    "Звук работающего двигателя прервал мой сеанс самоистязания."
    "Когда я открыл глаза, то увидел, как вновь поднялась метель после затишья."
    "Автобус приехал.{w} Несколько необычный, старый, какие чаще ходят в провинциальных городах, но тускло освещённая табличка «410» чуть выше лобового стекла развеяла сомнения. Мой маршрут."
    window hide
    $ renpy.pause(2)
    scene anim intro_10
    with fade
    #$ renpy.pause(3)
    play sound sfx_intro_bus_door_open # Самое интересное, по звуку это скорее close, с последующим стартом двигателя
    #scene anim intro_8  # Решние, в принципе, работает, но несколько теряется атмосфера. Можно выкинуть кадр с лицом вообще, например
    #with fade
    $ renpy.pause(3)
    scene anim intro_11
    stop sound fadeout 2
    with fade
    play music music_list["smooth_machine"] fadein 1
    window show
    "По ступенькам я поднялся навстречу свету, льющемуся из салона автобуса, и двери захлопнулись за моей спиной." # Менять сцену!
    "Красный автобус ЛиАЗ-677 оказался старым на вид не только снаружи. Поручни, сиденья — всё прямиком из прошлого века."
    "Ощутимо пахло выхлопными газами. Мягкий янтарный свет от ламп только дополнял эффект безнадёжно утраченной старины."
    "Я поискал взглядом хоть одно средство контроля оплаты проезда и не нашёл такого.{w} Даже валидатора с турникетом, которые в последнее время начали активно устанавливать во все автобусы, не было." 
    "Может быть, поэтому я так давно не видел ЛиАЗ в ходу, ведь турникет там легко не поставить."
    "Место кондуктора — отдельное сиденье с табличкой рядом, оповещающей, кому оно принадлежит — пустовало, поэтому я двинулся к застеклённой кабине водителя." 
    "В окне была сделана сдвижная форточка для приёма денег."
    "Билет на одну поездку стоил двадцать рублей." 
    "Я, сжав деньги, постучал в окошко, немедленно открывшееся."
    me "Возьмите оплату за проезд, пожалуйста..."
    "Водитель небрежно отвёл мою руку, словно слепец, который внезапно решил отказаться от подачки."
    vd "Можешь оставить себе.{w} С Рождеством."
    "В отражении зеркала заднего вида я заметил, как водитель недобро улыбнулся."
    "Я замешкался."
    th "Неважно, зато сэкономлю деньги на обратный путь."
    "На миг показалось, что водитель повернулся, и я увидел его лицо, но мне было уже не до этого, я занял место на сиденье у двери в правой половине салона."
    play sound sfx_intro_bus_door_open fadein 10  # Если здесь будет смена фона, можно сделать лучше.
    $ volume(0.5, "sound")
    "И только тогда автобус тронулся с места, слегка заваливаясь корпусом в сторону тротуара."
    "Мерно тарахтящий гул мотора успокаивал."
    window hide
    $ renpy.pause(1)
    scene bg intro_xx
    with dissolve
    window show
    "Перед тем как прислониться к стеклу, я взглянул на бесконечное движение за окном слева."
    "Машины, блеск витрин магазинов, серые фигуры людей, мятущихся в ожидании зелёного света, — все эти проявления жизни вечерней Москвы навевали тоску, и я вскоре отвернулся, задумавшись, что хорошо было бы прогуляться в безлюдном парке после Макдональдса."
    "Автобус проехал тот перекрёсток, но замедлил ход перед следующим и остановился на светофоре."
    "Я прислонился к стеклу, удивительным образом не чувствуя холода."
    "Усталость одолевала меня, совсем как тогда в кресле перед компьютером."
    "Освещение в автобусе неожиданно погасло." # Спецэффекты!
    "Похоже, я засыпал.{w} Всё, что я видел, потеряло чёткие очертания, как от выступивших на глазах слёз."
    "Где-то в темноте вечера, за хаотично прилипшими к стеклу снежинками, горел светофор - его диск расплылся красным пятном."
    "Я не заметил, когда друг за другом зажглись жёлтый и зелёный свет, и автобус помчался, проехав нужную мне остановку."
    stop music fadeout 2
    window hide
    scene anim intro_13
    with fade2
    $ renpy.pause(3, hard=True)
    play music music_list["door_to_nightmare"] fadein 2 #Можно таки шум мотора убрать
    window show
    "Он поехал дальше, словно водитель забыл о единственном пассажире. Автобус шёл на разгон, набирая скорость."
    "Усталость лишила меня сил бояться, сопротивляться и требовать немедленно остановить автобус, и мне оставалось лишь наблюдать за стремительно меняющимся пейзажем за окном."
    "В какой-то момент я проглядел остановку у странных ворот, а потом автобус снова набрал такую безумную скорость на идеально ровной дороге, что свет фонарей слился в одну размытую полосу."
    "А дальше начался кошмар." # Текст без изображения
    "Замедлившийся автобус объяло сполохами фиолетового пламени.{w} Неожиданно включившийся трескучий голос диктора звучал как запись, поставленная задом наперёд."
    "Впереди мелькнула стена, сквозь которую пронёсся автобус."
    "Я не понимал, снится ли мне всё или происходит наяву."
    "Как же я хотел, чтобы всё оказалось плохим сном!"
    "Меня кидало, толкало и трясло, но я не сделал ничего, чтобы удержаться на месте.{w} Казалось, что я сросся с креслом, и только это не давало мне слететь на пол."
    "Автобус вылетел из темноты на разбитый асфальт широкой дороги между улицами страшного города."
    "Невысокие дома на обочинах проседали набок, точно косые доски в заборе, лишённые стёкол окна чернели глазницами."
    "За окном было видно, как из низко повисшего красного неба медленно сыпал пепельно-чёрный снег."
    "Печальное зрелище вымершего города наводило на мысль, что наступил конец света."
    "Всё плыло перед глазами, будто я хлебнул вина с ядом и, не подозревая о приближающейся смерти, пустился в танец с отравителем, а он, смеясь, заставлял меня кружиться всё быстрее и быстрее..."
    "В автобусе появился ещё один человек - девушка с сумкой через плечо.{w} Толком рассмотреть её не удалось. Я потерял сознание."
    window hide
    stop sound_loop fadeout 1 # И убрать музыку
    stop music fadeout 1 # И убрать музыку
    scene black
    with dissolve
    $ renpy.pause(5, hard=True)
    $ volume(1, "sound")
    jump ii_eroge_d1
