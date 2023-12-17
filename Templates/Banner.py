def print_banner():
    
    print(r"""
      ______  __    __   __  .___  ___.  _______ .______          ___      
     /      ||  |  |  | |  | |   \/   | |   ____||   _  \        /   \     
    |  ,----'|  |__|  | |  | |  \  /  | |  |__   |  |_)  |      /  ^  \    
    |  |     |   __   | |  | |  |\/|  | |   __|  |      /      /  /_\  \   
    |  `----.|  |  |  | |  | |  |  |  | |  |____ |  |\  \----./  _____  \  
     \______||__|  |__| |__| |__|  |__| |_______|| _| `._____/__/     \__\ 
     
     &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&############################&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&###############BBBBBBBBBBBBBBBBB##############&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&###########BBBBBBGGGPP55YYYYJJJYYY555PPGGBBBBB############&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&########BBBBBBGGGGPP55YJ??77!!!!~~~!!!!77??JY55PPGGGBBBBBBB########&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&#####BBBBBBGGGGGPP55YJJ??7!!~^^^^::::::::^^^~~!77?JJY55PPGGGGGBBBBB#######&&&&&&&&&&&&&
&&&&&&&&&&####BBBGGGGGPPPP555YYYPGB##BBGP5Y?7!!77..77!!7?Y5GGBBBBBGP5YY55PPPGGGGBBBBBB####&&&&&&&&&&
&&&&&&&####BBGGGPPPPP555YYY5P#&#BP555PPPPPPPPG#B:..^##G55PP5555555PB#&#P5Y5555PPPPPPPGGGB###&&&&&&&&
&&&&&####BGGP555555YYYYJJ??5#BPG#&&&##BBB##&#G7.7@@!.JB###BGGB###&&#GPB#P?JJJYYYYYYYYYY5PGB###&&&&&&
&&&####BGGP5YYJJJJJJJ???77BB5B&#PJJ5B#&#BPJ77!^ .YY..^7?7JPB###B5?JP#&#5BB??????????77??JYPGB###&&&&
&#####BGP5YJ??????7777777#BJGP?77?JYYJJJYP&@#YJG7  ?GJYB@#5J???JY?7!!?5BYG#777!!!!!!!!!!7?J5GB###&&&
#####BGPYJ77!!!!!7YPGGGPG##&#G#&&&&&&#P7~!YB&@&Y&###Y&@#GJ~~?P#&&&&&&BG#&##GGGGG5J!^~~~~~!7J5GB####&
####BGPY?7!~~~~?GB5!:.    .:G&P7~:::^?##7JY?.^&@B@@B@&:.JYYY&#!::::^7G@5..    .:!YGG7^^^^~~7J5GB####
##BBGPY?!~~^:!##?^:^~YPGP5^?J.       !?7PJ?^  .@@@@@@.  ^??577!       .??!5PGPJ~:..7BB!:^^^~7YPGB###
#BBGP5J7~^^:?@P~!J5~J@@@&#!P.       G?~B@~Y.   !@@@@^   .?!@G^PY        5?&@@@@Y~Y?~~5@7::^^!?YPGB##
BBGP5J7~^::~@P!YG5~.:@@&@&~Y.      .@Y^@@#?J:   .J7    :77#@&^G@       .J7@@&@@. !YGJ!P@^.:^~!J5PGBB
GGP5J7!^::.G@75@Y? ..BB@@@#77:      @@55@@&#G?^:^^^^:^?5B&@@YG@&      :7?&@@@GP   YY&??@5.::^~7JYPGG
P5YJ7!^::..#&Y@@J7 .  #@@@@@BY7^.   :&@&B##GGG#5^::^P#PGG#&B@@&.   .^75#@@@@@P    JY@&J@B...:^~7?Y5P
YJ?7!^::...G@@@@PY.   ^@@@@@@@@&G5?!^7YYY7&??J7P!PG!P!Y??#!YYY7~!J5B&@@@@@@@@.   .YB@@&@Y ...:^~!7JY
?7!~^::... ^@@@@@GJ.   ^P75B&@@@@@@&P7~~~J@&P#57B@@G75#P&@?~~~?G&@@@@@@&BY7G:   :YB@@@@&......:^~~!7
!!~^::..... ~@@@@@&P!.       .^JG&@@@&&@@&B&5!Y&?775&J7G&#@@@&&@@@#5!:        :?G&@@@@&: ......::^~~
~^::......   .P@@@@@@#57^..       :5@@BB@&P!YB5BG^^#BPG?!B@@B#@@7        ..^?G&@@@@@@Y.    ......::^
^::......      .?#@@@@@@@&&&#BGY!.  &@@Y@#BGYYG@Y^^5@GJYGG&@J@@B  :?PGB#&&&@@@@@@@B7.        ......:
:.......          .^?P#&@@@@&BY!.  ~@@B#B@##@&J!~~~~!Y&@G#@BB#@@:  :7P#&@@@&&BP?:             ......
......      ^5B^                  ?@@GGG#@@GP@&~PBB5^#@YG@@BGG#@@7                  ~#Y:        ....
....       G@@&                .?#&BGG&P&@@@~P&@&BB&&&Y7@@@&G#GG#@#7.                @@@5         ..
..        .@@@@G^.         :!5#&&&#&@@55@@@@YBBG5GPYGBB5@@@@YG@@&#&@&BY~.         .~B@@@@           
           :G&@@@@@&####&@@@@@&GY?~B@#^@@@@@@@&5&@@#5&@@@@@@@:&@Y^?YG&@@@@@&####&@@@@@@G:           
              .~?YPGBBGG5J7~:.   ^7^B@^#@@@@@@@@#B#&@@@@@@@@B~@P^7.    :~7J5GGBGGPY?~:              
                                  7Y!5#!5@@@&@@@@@@@@@@&@@&Y?#Y?5^                                  
                                   ^P5JP5JPB7@@@@@@@@@@!G5JPPYPP:                                   
                                     ?GP5P5Y~G@@@@@@@@P:J5P5GG!                                     
                                      .7PBJGPPB@@@@@@BYPPYBP!.                                      
.........................................^!&P@!&@@@@&!@P#!^.........................................
:::::::::::::::::.................::::::::^@P@YP@@@@PY@G&::::::::::::::::.......::::::::::::::::::::
^^^^^^^^^^^^^^^^^^^::::::::::::::^^^^^^^^^~GP@G@5&&P@P@GP^~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
!!!!!!!!!~~~~~~~~~~~^^^^^^^^^^^^~~~~~~~~~~!~J@G@5&&5@P@J~!!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
777777777!!!!!!!!!!!~~~~~~~~~~~!!!!!!!!!!!!!!G5@P@@P@5G77777!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
?????????77777777777777!!!!!777!77777777777777!B5@@5B!7777777777777777777777777777777777777777777777
JJJJJJJJJJ???????????????????????????????JJJJJJJ?&&?JJJJJJJ???????????????????????????????JJJJJJ????
JJJJJJJJJJJJJJJJYYYYY5555PPPGGGBBBB####&&&&&&&&&&#&&&&&&&&&&###BBBGGGPPPP55555YYYYYYYJJJJJJJJJJJJJJJ
JJJJJJJJJJJJJJJYYYYY55555PPPGGBBB###&&&&@@@@@@@@@@@@@@@@@@&&&&###BBBGGPPP55555YYYYYYYJJJJJJJ??JJ????
77777777777777777777?????????JJJJJYYYYY555555PPPPPPP55555555YYYYYJJJJJJ????????777777777777777777777
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
^^^^:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::^^^
:::::::::::::::::::::::::::::::::::::::::::::::::::::::..........:::::::::::::::::::::::::::::::::::
                                                                        
    """)