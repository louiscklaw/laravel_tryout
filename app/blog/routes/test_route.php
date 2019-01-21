<?php


Route::get('/test', function(){
    $flights = App\Flight::all();

    $acc_string = array();
    foreach($flights as $flight)
    {
        echo $flight->test_field1;
    }
});
