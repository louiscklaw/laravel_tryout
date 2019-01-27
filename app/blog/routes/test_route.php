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

Route::get('/test_blankpage', function () {
    return view('blankpage');
});

Route::get('/test_form', function () {
    return view('form_basic');
});

Route::get('/test_menu', function () {
    $test_menuitem1=array();
    $test_menuitem1['name']='test menuitem1';
    $test_menuitem1['icon'] = 'content_copy';

    $test_menuitem2=array();
    $test_menuitem2['name']='test menuitem2';
    $test_menuitem2['icon'] = 'content_copy';



    return view('form_basic', [
        'active_menu' => 'Typography',
        'menuitems' => ['menuitem1','menuitem2'],
        'test_menuitems'=>[$test_menuitem1, $test_menuitem2]
    ]);

});
