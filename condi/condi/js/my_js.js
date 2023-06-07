
    //відкривачка фільтрів
    function open_or_hide_filters(filter) {

        if (filter.classList.contains('filter_active')) {

            filter.classList.remove('filter_active')
            filter.children[1].style.opacity = '0'
            filter.children[0].style.zIndex = '10'
            filter.children[1].style.zIndex = '10'
            setTimeout(() => {
                filter.children[1].style.display = 'none'

            }, 200)
            filter.children[0].children[2].style.transform = 'rotate(0deg)'

        } else {
            
            filter.classList.add('filter_active')
            filter.children[0].style.zIndex = '14'
            filter.children[1].style.zIndex = '13'
            filter.children[1].style.display = 'block'
            filter.children[0].children[2].style.transform = 'rotate(180deg)'

            setTimeout(() => {
                filter.children[1].style.opacity = '1'
            }, 0)
        }
    }


    // зміна фільтрів
    // option змінна яка містить _p_ 
    function filter(option) {
        // pk змінна яка містить атрибут з _р_
        const pk = option.getAttribute('pk')
        // filter змінна яка містить діда _р_
        const filter = option.parentNode.parentNode


        if (option.classList.contains('option_active')) {
            //відбираємо клас
            option.classList.remove('option_active')
            // відбираємо фільтер у дідового _р_(вертаємо базу)
            filter.children[0].children[1].textContent = filter.children[0].children[1].getAttribute('base_text')
            // вертаємо базовий індекс елемента
            filter.setAttribute('select_pk', null)
            // прибираємо хрестик з фільтра
            filter.children[0].children[0].classList.remove('img_close_active')
        } else {
            // дістаємо список дітей
            let children_list = option.parentNode.children
            // перераховуємо дітей
            for (let i = 0; i < children_list.length; i++) {
                // якщо діти є _р_ 
                if (children_list[i].tagName == 'P') {
                    // і якщо вони містять активний клас
                    if (children_list[i].classList.contains('option_active')) {
                        // відбираємо його у дітей
                        children_list[i].classList.remove('option_active')
                    }
                }
            }
            //надаємо клас
            option.classList.add('option_active')
            // даємо індекс дітятка (фільтра)
            filter.setAttribute('select_pk', pk)
            // даємо контент дітятка
            filter.children[0].children[1].textContent = option.textContent
            // добавляємо хрестик для видалення дітятка
            filter.children[0].children[0].classList.add('img_close_active')
        }
    }






    // клік по хрестику
    function filter_off(hrest) {
        // children_list містить всіх дітяток (_р_; _hr_)
        let children_list = hrest.parentNode.parentNode.children[1].children
        for (let i = 0; i < children_list.length; i++) {
            // якщо дітятко має option_active
            if (children_list[i].classList.contains('option_active')) {
                // запускає попередню функцію і по кліку на хрестик видяля дітьо 
                filter(children_list[i])
            }
        }
    }





