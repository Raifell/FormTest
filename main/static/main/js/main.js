var count = 1;


function plus(){
    let form = document.getElementById('example-form')
    let button = document.getElementById('submit')
    let p = document.createElement('p')
    let label = document.createElement('label')
    label.innerText = 'Track: '
    let input = document.createElement('input')
    input.name = 'url' + count
    count += 1
    input.type = 'file'

    p.appendChild(label)
    p.appendChild(input)

    button.before(p)
};
