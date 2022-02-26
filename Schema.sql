create table question_list
(
    question_id integer primary key,
    question    varchar(64),
    image_url   varchar(256)
);
insert into question_list (question_id, question, image_url)
values (1, '体を動かすことが好きだ',
        'https://3.bp.blogspot.com/-6xlmgmkp8Nw/Vq89C1lw3EI/AAAAAAAA3k4/ouvm013IDoI/s800/junbiundou_shinkyaku.png');
insert into question_list (question_id, question, image_url)
values (2, 'ワイワイするのが好きだ',
        'https://1.bp.blogspot.com/-y2aRIisq9VU/Wq9-ZUZOUPI/AAAAAAABK8g/uHSy6Db5ARIsTNdzdyVS9AQzMGOY-8DPQCLcBGAs/s500/group_kids_no_dog.png');
insert into question_list (question_id, question, image_url)
values (3, 'コンテストに参加したい',
        'https://3.bp.blogspot.com/-HvtSRPVSLdM/WWXXCMNXqAI/AAAAAAABFew/RxIi8UEWa2EeynH9A_gkY-SDvKuQmfYGwCLcBGAs/s500/machine_robot_contest_big.png');
insert into question_list (question_id, question, image_url)
values (4, '結果よりプロセスが重要だ',
        'https://2.bp.blogspot.com/-bQYANW7prHw/Wc8f8soXACI/AAAAAAABHJc/ErtDG5TFSLggiJjEGONoHGPMkoW-9fqwwCLcBGAs/s400/study_woman_normal.png');
insert into question_list (question_id, question, image_url)
values (5, 'モノづくりが好きだ',
        'https://1.bp.blogspot.com/-y8MKc7pK_go/XkZcwbGxPwI/AAAAAAABXPY/PgpIekCPv8gO5TzHkdbT_irR1coyPul3QCNcBGAsYHQ/s400/computer_hacker_white1_woman.png');
insert into question_list (question_id, question, image_url)
values (6, '人前で話すのが得意だ',
        'https://1.bp.blogspot.com/-SJtAUFka3hA/VRUSRSC57EI/AAAAAAAAsok/uycjU9YqOXA/s400/speech_man.png');

create table answer_table
(
    game_id     varchar(64),
    question_id integer NOT NULL,
    answer      boolean NOT NULL,
    PRIMARY KEY (game_id, question_id)
);
insert into answer_table (game_id, question_id, answer)
values ('314b8c3b-7dc3-479a-906d-8be9a8bcda4b', 2, 1);
insert into answer_table (game_id, question_id, answer)
values ('972d0915-1421-444d-ac57-2eacac082bd9', 1, 1);
insert into answer_table (game_id, question_id, answer)
values ('ca0da351-3b1c-4fd3-a369-798027de9260', 1, 0);
insert into answer_table (game_id, question_id, answer)
values ('314b8c3b-7dc3-479a-906d-8be9a8bcda4b', 1, 1);
insert into answer_table (game_id, question_id, answer)
values ('314b8c3b-7dc3-479a-906d-8be9a8bcda4b', 3, 0);
insert into answer_table (game_id, question_id, answer)
values ('314b8c3b-7dc3-479a-906d-8be9a8bcda4b', 4, 1);
insert into answer_table (game_id, question_id, answer)
values ('314b8c3b-7dc3-479a-906d-8be9a8bcda4b', 5, 1);


create table circle_list
(
    circle_id   integer primary key,
    circle_name varchar(32)
);
insert into circle_list (circle_id, circle_name)
values (0, 'LTサークル');
insert into circle_list (circle_id, circle_name)
values (1, 'Unityサークル');
insert into circle_list (circle_id, circle_name)
values (2, '麻雀サークル');
insert into circle_list (circle_id, circle_name)
values (3, 'プログラミングサークル');
insert into circle_list (circle_id, circle_name)
values (4, 'カーリングサークル');
insert into circle_list (circle_id, circle_name)
values (5, 'カバディサークル');
insert into circle_list (circle_id, circle_name)
values (6, 'トライアスロン部');
insert into circle_list (circle_id, circle_name)
values (7, '鳥人間サークル');


create table master_point_handler_tbl
(
    circle_id  integer primary key,
    question_1 boolean,
    question_2 boolean,
    question_3 boolean,
    question_4 boolean,
    question_5 boolean,
    question_6 boolean
);
insert into master_point_handler_tbl (circle_id, question_1, question_2, question_3, question_4, question_5,
                                           question_6)
values (1, 1, 1, 1, 1, 1, 1);
insert into master_point_handler_tbl (circle_id, question_1, question_2, question_3, question_4, question_5,
                                           question_6)
values (2, 0, 0, 1, 1, 1, 0);
insert into master_point_handler_tbl (circle_id, question_1, question_2, question_3, question_4, question_5,
                                           question_6)
values (3, 0, 1, 0, 0, 0, 0);
insert into master_point_handler_tbl (circle_id, question_1, question_2, question_3, question_4, question_5,
                                           question_6)
values (4, 0, 0, 0, 1, 1, 1);
insert into master_point_handler_tbl (circle_id, question_1, question_2, question_3, question_4, question_5,
                                           question_6)
values (5, 1, 1, 0, 0, 0, 0);
insert into master_point_handler_tbl (circle_id, question_1, question_2, question_3, question_4, question_5,
                                           question_6)
values (6, 1, 1, 0, 0, 0, 1);
insert into master_point_handler_tbl (circle_id, question_1, question_2, question_3, question_4, question_5,
                                           question_6)
values (7, 1, 0, 0, 0, 0, 0);
insert into master_point_handler_tbl (circle_id, question_1, question_2, question_3, question_4, question_5,
                                           question_6)
values (8, 1, 1, 1, 0, 1, 0);


create table point_rule
(
    question_id int,
    cicle_1     int,
    cicle_2     int,
    cicle_3     int,
    cicle_4     int,
    cicle_5     int,
    cicle_6     int,
    cicle_7     int,
    cicle_8     int
);
insert into point_rule (question_id, cicle_1, cicle_2, cicle_3, cicle_4, cicle_5, cicle_6, cicle_7, cicle_8)
values (1, 1, 0, 0, 0, 1, 1, 1, 1);
insert into point_rule (question_id, cicle_1, cicle_2, cicle_3, cicle_4, cicle_5, cicle_6, cicle_7, cicle_8)
values (2, 1, 0, 1, 0, 1, 1, 0, 1);
insert into point_rule (question_id, cicle_1, cicle_2, cicle_3, cicle_4, cicle_5, cicle_6, cicle_7, cicle_8)
values (3, 1, 1, 0, 0, 0, 0, 0, 1);
insert into point_rule (question_id, cicle_1, cicle_2, cicle_3, cicle_4, cicle_5, cicle_6, cicle_7, cicle_8)
values (4, 1, 1, 0, 1, 0, 0, 0, 0);
insert into point_rule (question_id, cicle_1, cicle_2, cicle_3, cicle_4, cicle_5, cicle_6, cicle_7, cicle_8)
values (5, 1, 1, 0, 1, 0, 0, 0, 1);
insert into point_rule (question_id, cicle_1, cicle_2, cicle_3, cicle_4, cicle_5, cicle_6, cicle_7, cicle_8)
values (6, 1, 0, 0, 1, 0, 1, 0, 0);


create table admin_table
(
    user_id   varchar(32) primary key,
    user_pass varchar(32)
);
insert into admin_table (user_id, user_pass)
values ('testuser_01', 'qwertyui');
insert into admin_table (user_id, user_pass)
values ('testuser_02', 'asdfghjk');
insert into admin_table (user_id, user_pass)
values ('testuser_03', 'zxcvbnm,');
