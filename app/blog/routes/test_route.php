<?php

use Illuminate\Support\Facades\Auth;


Route::get('/test', function(){
    $flights = App\Flight::all();

    $acc_string = array();
    foreach($flights as $flight)
    {
        echo Auth::user();

    }
});
