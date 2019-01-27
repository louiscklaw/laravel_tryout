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
    $test_menuitem1['father']=null;
    $test_menuitem1['name']='Home';
    $test_menuitem1['icon'] = 'content_copy';

    $test_menuitem2=array();
    $test_menuitem2['father']=null;
    $test_menuitem2['name']='Typography';
    $test_menuitem2['icon'] = 'content_copy';

    $test_menuitem3=array();
    $test_menuitem3['father']='Typography';
    $test_menuitem3['name']='Typography1';
    $test_menuitem3['icon'] = 'content_copy';

    return view('form_basic', [
        'active_menu' => 'Typography',
        'test_menuitems'=>array(
            $test_menuitem1, $test_menuitem2, $test_menuitem3   )
    ]);

});
