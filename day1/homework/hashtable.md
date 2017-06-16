```py
# hash table is a collection of unique key-value pairs. Similar to set() as it stores unique keys but 
# this one has (key, value)s.
table = {}
fruits = ['apple', 'apple', 'kimchi']
for i,fruit in enumerate(fruits):
    if i % 2:
        table[fruit] = 'depends'
    else:
        table[fruit] = 'good'
```
# => table = {apple: good, kimchi: depends}
```js
let table = JSON.parse(axios.get('www....'));
/*
table = {
    'id': 'blhah',
    'hello': 'world
    ...
}
*/
```

### Definitely google hashmap for more details. Good to know how hashmap or hashtable actually built.
