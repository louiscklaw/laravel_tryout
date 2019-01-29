<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;

// https://laravel.com/docs/5.7/blade#components-and-slots
use Illuminate\Support\Facades\Blade;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Bootstrap any application services.
     *
     * @return void
     */
    public function boot()
    {
        //
        Blade::component('layouts.components.alert','alert');

        Blade::component('layouts.components.textInput','textInput');
        Blade::component('layouts.components.passwordInput','passwordInput');
        Blade::component('layouts.components.card_inside_title','card_inside_title');

        Blade::component('layouts.components.card','card');
        Blade::component('layouts.components.card_inside','card_inside');

    }

    /**
     * Register any application services.
     *
     * @return void
     */
    public function register()
    {
        //
    }
}
