use strict;
use warnings;
use Cwd;
use File::Copy;
use File::Basename;
#+---------------------------------------------------+
#|                                                   |
#|               !#########       #                  |
#|             !########!          ##!               |
#|          !########!   Union of    ###             |
#|       !##########      Soviet      ####           |
#|     ######### #####     IIchan     ######         |
#|      !###!      !####!   Republics  ######        |
#|        !           #####            ######!       |
#|                      !####!         #######       |
#|                         #####       #######       |
#|                           !####!   #######!       |
#|                              ####!########        |
#|           ##                   ##########         |
#|         ,######!          !#############          |
#|       ,#### ########################!####!        |
#|     ,####'     ##################!'    #####      |
#|   ,####'            #######              !####!   |
#|  ####'                                      ##### |
#|  ~##        ALL HAIL THE MOTHERLAND!          #~  |
#|                                                   |
#+---------------------------------------------------+
# =======
# глобали
# =======
my $path 		= cwd();
my $prefix		= "";		# префикс
my $affix		= "_old";	# постфикс
#my $extension	= ".jpg";	# расширение переименовываемых файлов
opendir (DIR, $path) or die $!;
#my @files = grep { /.jpg$/ } readdir(DIR);	# выбрать все файлы, содержащие в названии строку ".jpg" в конце "$"
my @files = readdir(DIR);

foreach (@files) {
	my ($extension) = $_ =~ /(\.[^.]+)$/;
	my ($filename)  = $_ =~ /(\w+)/;
    move($_, $prefix . $filename . $affix . $extension);
	print $prefix . $filename . $affix . $extension . "\n";
}

closedir(DIR);
