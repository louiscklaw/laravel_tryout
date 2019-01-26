@extends('auth.app')

@section('body')

<body class="login-page">
    <div class="login-box">
        <div class="logo">
            <a href="javascript:void(0);"><b>LOGIN : </b></a>
            <small>ACME corp</small>
        </div>

        @include('auth.login_card')

    </div>

    @include('auth.body_scripts')

</body>
@endsection
