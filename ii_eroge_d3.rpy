# ===============
# День 3 (третий)

# =========================
# Сцена первая. Пробуждение

	# "Утренний" фильтр на фоны - чуть затемнить и больше жёлтого и оранжевого спектра.
	"Я открыл глаза."
	"Тишина."
	"Ветер нежно шелестит кронами за окном."
	"Ольга Дмитриевна мирно сопит."
	"Проснулся до подъема"
	"Сон без сновидений."	
	"В лагере меня совсем не посещают сны."
	
	# ВЫБОР
	# 	1	Встать и пойти на пробежку и на турники.
		me "Проснулся так проснулся. Нет смысла валяться. Наступает новый день, проснись и пой строна родная."
		"Расталкивая остатки сновидений, я возвращался в мир будня."
		"Удалось одеться и не разбудить вожатую." # интересно, снятся ли ей сны про слонов у стены
		# Сила +1.
		th "Лагерь спит. Приятное ощущение."
		"Решил пробежаться до спортплощадки"
		"Заметил что я не один"

		# ===========================
		# Сцена вторая. Спорт и Славя
		"К своему удивлению, на спортплощадке я был не один. Здесь уже занималась девушка."
		"Ловко размахивая руками и выгибая спину она разминалась."
		"Пока не заметила меня."
		"Славя."
		me "Доброе утро!"
		sl "Доброе!"		
		# Вместе они так и проведут время до основной зарядки 
		# Основная зарядка
		# jump d3_scene_utro_lineika

	#	2	Вспомнить сновидения
		"Меня это тревожило, так как сны были важной частью моей жизни."
		"Мне захотелось вспомнить что мне снилось."
		"В одной книге я читал, что нужно расслабиться и закрыть глаза, притвориться спящим, чтобы встревоженные зарёй сновидения вернулись во взъерошенную голову."
		"Меня прошиб холодный пот"
		"Снилась девочка из автобуса" | "Снилась Криппи"
		"Остались следы" # а-ля ссадины на ладони | что-либо ещё
		# Пропускает зарядку
		# jump d3_scene_utro_lineika
	
	# =============================================
	# Сцена третья. Утренняя линейка и День Нептуна
	# На линейке объявляют мероприятие: с двух до девяти вечера в лагере - Праздник Нептуна.
	# Семён даже не подозревает, что его ждёт... Для тех, кто не желает участвовать, остаётся тихий час.
	# d3_scene_utro_lineika:
