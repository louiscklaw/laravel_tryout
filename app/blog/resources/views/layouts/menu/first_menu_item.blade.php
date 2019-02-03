<li>
    <li class="active">

    {{$contain_second_menu_items = isset($left_menu[$cur_pos]['submenu'])}}

    @if (isset($contain_second_menu_items) && ($contain_second_menu_items))
        <a href="javascript:void(0);" class="menu-toggle waves-effect waves-block toggled">
    @else
        <a href="javascript:void(0);" class="waves-effect waves-block toggled">
    @endif
        @if (isset($widget))
            <i class="material-icons">{{$widget}}</i>
        @endif
        <span>{{ $slot }}</span>
    </a>
    </li>
    @if (isset($contain_second_menu_items) && ($contain_second_menu_items))
        <ul class="ml-menu" style="display: block;">
            <li>
            @foreach($left_menu[$cur_pos]['submenu'] as $menu_entry)
                @component('layouts.menu.second_menu_item')
                    {{$menu_entry['text']}}
                @endcomponent
            @endforeach
            </li>
        </ul>
    @endif
</li>
