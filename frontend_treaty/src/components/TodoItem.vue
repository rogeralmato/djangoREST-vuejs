<template>
    <div class="todo-item">
        <div class="todo-item-left">
                <input type="checkbox" v-model="todo.completed">
                <div v-if="!todo.editing" class="todo-item-label" :class="{completed : todo.completed}" 
                    @dblclick="editTodo(todo)">{{todo.title}}</div>
                <input v-else class="todo-item-edit" type="text" v-model="todo.title" 
                    @blur="doneEdit(todo)" @keyup.enter="doneEdit(todo)" @keyup.esc="cancelEdit(todo)" v-focus>
        </div>
        <div class="remove-item" @click="removeTodo(index)">
            &times;
        </div>
    </div>
</template>

<script>
export default {
    name: 'todo-item',
}
</script>

<style lang="scss">

</style>