<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Flight extends Model
{
    //
    protected $table = 'my_fight';
    public $timestamps = false;
    protected $dateFormat = 'U';
}
