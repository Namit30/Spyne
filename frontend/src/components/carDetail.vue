<template>
    <div>
      <h2>{{ car.title }}</h2>
      <p>{{ car.description }}</p>
      <div v-if="Array.isArray(car.tags)">
        <span v-for="tag in car.tags" :key="tag">{{ tag }}</span>
      </div>
      <button @click="deleteCar">Delete</button>
      <button @click="editCar">Edit</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'CarDetail', // Multi-word name as per Vue conventions
    props: ['car'],
    methods: {
      deleteCar() {
        this.$emit('deleteCar', this.car.id);
      },
      editCar() {
        this.$emit('editCar', this.car);
      },
    },
  };
  </script>
  