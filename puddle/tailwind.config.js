/** @type {import('tailwindcss').Config} */

module.exports = {
    content: [
        'puddle/core/templates/core/*.html',
        'puddle/core/static/core/*.css',
        'puddle/item/templates/item/*.html',
    ],
    theme: {
        extend: {
            fontSize: {
        
                '4xl': '2.5rem',
                '3xl': '2rem',
                '2xl': '1.5rem',
                'xs': '.5rem',
                '5xl': '3rem',
                '6xl': '4rem',
                '7xl': '5rem',
                '8xl': '6rem',
            },
        
            fontFamily: {
                'robo': ["Roboto Slab", 'serif'], 
                'brush': ["Sickness Lines", 'sans-serif'],
            },
            borderWidth: {
                'dotted': '1px',
            },
        },
        plugins: [],
    }
}