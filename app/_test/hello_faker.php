<?php
    // require the Faker autoloader
    require_once './vendor/fzaninotto/faker/src/autoload.php';
    // alternatively, use another PSR-0 compliant autoloader (like the Symfony2 ClassLoader for instance)
    echo 'start';

    // res, config
    $PDO_CONFIG = strtr(
        'mysql:host=hostname;dbname=defaultDbName',
        array(
            'hostname'=>'localhost',
            'defaultDbName'=>'faker_test'
        )
        );

    $MYSQL_ADMIN_PASS = getenv('MYSQL_ADMIN_PASS');


    // src
    // use the factory to create a Faker\Generator instance
    $faker = Faker\Factory::create('zh_HK');

    // generate data by accessing properties
    // echo $faker->name;
    // 'Lucy Cechtelar';
    // echo $faker->address;
    // "426 Jordy Lodge
    // Cartwrightshire, SC 88120-6700"
    // echo $faker->text;

    // Dolores sit sint laboriosam dolorem culpa et autem. Beatae nam sunt fugit
    // et sit et mollitia sed.
    // Fuga deserunt tempora facere magni omnis. Omnis quia temporibus laudantium
    // sit minima sint.

    $pdo = new PDO($PDO_CONFIG, 'admin', $MYSQL_ADMIN_PASS);
    $sql = 'INSERT INTO test_table (firstName, lastName, regDate, regEmail, acDisabled, comment) VALUES (?,?,?,?,?,?)';
    $stmt = $pdo->prepare($sql);

    $insertedPKs = array();
    for ($i=0; $i < 999; $i++) {
        try {
            $stmt->bindValue(1, $faker->firstName, PDO::PARAM_STR);
            $stmt->bindValue(2, $faker->lastName, PDO::PARAM_STR);
            $stmt->bindValue(3, $faker->date, PDO::PARAM_STR);
            $stmt->bindValue(4, $faker->email, PDO::PARAM_STR);
            $stmt->bindValue(5, $faker->randomElement($array = array(0, 1)), PDO::PARAM_STR);
            $stmt->bindValue(6, $faker->randomElement($array = array(
                    join(' ', $faker->words($nb = 3, $asText = false)),
                    $faker->sentence($nbWords = 6, $variableNbWords = true),
                    $faker->realText()
                )), PDO::PARAM_STR);
            $stmt->execute();
            $insertedPKs[]= $pdo->lastInsertId();
        } catch (\Throwable $th) {
            throw $th;
        }

        // var_dump($stmt);
    }

    echo 'done';
