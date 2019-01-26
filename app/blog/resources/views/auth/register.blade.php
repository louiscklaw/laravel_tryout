@extends('auth.app')

@section('body')
<body class="signup-page">
    <div class="signup-box">
        <div class="logo">
            <a href="javascript:void(0);"><b>REGISTER : </b></a>
            <small>ACME COPS</small>
        </div>
        @include('auth.register_card')
    </div>

    @include('auth.body_scripts')

</body>
@endsection
