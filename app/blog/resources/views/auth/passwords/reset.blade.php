@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-8">
            @include('auth.passwords.reset')
        </div>
    </div>
</div>
@endsection
