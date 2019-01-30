<!-- checkbox.blade.php -->
<input type="checkbox" id="{{ $checkbox_id }}" class="{{ isset($filled_in)? 'filled-in' : '' }}"
    {{ isset($checked)? 'checked' : '' }}
    {{ isset($disabled)? 'disabled' : '' }}
/>
<label for="{{ $checkbox_id }}">{{ $slot }}</label>
