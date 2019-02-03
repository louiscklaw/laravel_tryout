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

    $TXT_EN_HOME = 'home';
    $TXT_HOME = $TXT_EN_HOME;

    $left_menu=array(
        'Home'=>array(
            'text'=>$TXT_HOME,
            'icon'=>'home'
        ),
        'Typography'=>array(
            'text'=>'Typography',
            'icon'=>'text_fields'
        ),
        'Helper Classes'=>array(
            'text'=>'Helper Classes',
            'icon'=>'layers'
        ),
        'Widgets'=>array(
            'text'=>'Widgets',
            'icon'=>'layers',
            'submenu'=>array(
                'Cards'=>array(
                    'text'=>'Cards',
                    'submenu'=>array(
                        'Basic'=>array(
                            'text'=>'Basic'
                        ),
                        'Colored'=>array(
                            'text'=>'Colored'
                        ),
                        'No Header'=>array(
                            'text'=>'No Header'
                        ),
                    ),
                ),
                'Infobox'=>array(
                    'text'=>'infobox'
                )
            ),
        ),
    );

    return view('blank',['left_menu'=>$left_menu]);
});

Route::get('/basic_form', function(){
    return view('basic_form');
});

Route::get('/phpinfo', function(){
    return view('phpinfo');
});
