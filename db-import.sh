db.categories.insert([{
    title: 'some category',
    description: '',
    status: 'active', /* active|inactive */
    orderId: 1
}]);
db.posts.insert([{
    categoryId: 'a23rsd2fsd13r32rgsre42',
    userId: '12sd3rfsd23r23r',
    title: '1 post',
    slug: 'adsfasdf',
    text: 'adfewsdi akjshf alkhfdka asdlkfh aklsjdfk asdf askdjf',
    dateCreated: 1231231212,
    image: '/',
    source: 'http://mail.ru',
    status: 'draft', /* draft|moderated|deleted */
    hasVideo: true
}]);
db.users.insert([{
    login: '11',
    email: 'se@se.se',
    password: '12345',
    avatar: '',
    dateCreated: 143123152234,
    status: 'active', /* active|inactive */
    fio: '',
    country: '',
    sex: '',
    dateBirth: '',
    telephone: '',
    skype: ''
}]);