<?php

namespace Tests\Feature;

use Tests\TestCase;
use Illuminate\Foundation\Testing\RefreshDatabase;

class ExampleTest extends TestCase
{
    /**
     * A basic test example.
     *
     * @return void
     */
    public function testBasicTest()
    {
        $response = $this->get('/');

        $response->assertStatus(200);
    }

    public function testPagematerial_home()
    {
        $response = $this->get('/material_home');

        $response->assertStatus(200);
    }


    public function testPagebasic_form()
    {
        $response = $this->get('/basic_form');

        $response->assertStatus(200);
    }

}
