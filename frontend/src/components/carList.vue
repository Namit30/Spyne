<template>
    <div>
      <!-- Check if cars array is empty -->
      <div v-if="cars.length === 0">
        <p>No cars available</p>
      </div>
  
      <!-- List of cars -->
      <div v-for="car in cars" :key="car.id" class="car-item" @click="viewCar(car.id)">
        <h3>{{ car.title }}</h3>
        <p>{{ car.description }}</p>
        <div>
          <span v-for="tag in car.tags" :key="tag" class="tag">{{ tag }}</span>
        </div>
        <!-- Optionally add edit and delete buttons -->
        <button @click.stop="editCar(car)">Edit</button>
        <button @click.stop="deleteCar(car.id)">Delete</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: ['cars'],
    methods: {
      // Navigates to the individual car page when clicked
      viewCar(id) {
        this.$router.push(`/cars/${id}`);
      },
      // Emit the editCar event to parent component
      editCar(car) {
        this.$emit('editCar', car);
      },
      // Emit the deleteCar event to parent component
      deleteCar(id) {
        this.$emit('deleteCar', id);
      },
    },
  };
  </script>
  
  <style scoped>
  .car-item {
    border: 1px solid #ccc;
    padding: 10px;
    margin: 10px;
    cursor: pointer;
  }
  
  .car-item:hover {
    background-color: #f0f0f0;
  }
  
  .tag {
    margin-right: 5px;
    padding: 2px 6px;
    background-color: #f0f0f0;
    border-radius: 4px;
  }
  
  button {
    margin-top: 10px;
    margin-right: 5px;
    cursor: pointer;
  }
  </style>
  