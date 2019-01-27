<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class basicForm extends Model
{
    //
    protected $table = 'basic_form_test';
    public $timestamps = false;
    protected $dateFormat = 'U';

    protected $fillable = [
        'username', 'password',
    ];

}
