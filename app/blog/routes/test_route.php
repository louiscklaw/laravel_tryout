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


Route::get('/material_home', function(){
    return view('material_home');
});

Route::get('/blank', function(){
    return view('blank');
});

Route::get('/basic_form', function(){
    return view('basic_form');
});
