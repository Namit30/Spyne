<template>
    <div>
      <h1>Car Management</h1>
      <button @click="addNewCar">Add New Car</button>
  
      <!-- Display list of cars -->
      <div v-if="cars.length">
        <div v-for="car in cars" :key="car.id" class="car-card">
          <CarDetail :car="car" @deleteCar="deleteCar" @editCar="editCar" />
        </div>
      </div>
      <div v-else>
        <p>No cars available. Please add a new car.</p>
      </div>
  
      <!-- Add/Edit Car Form -->
      <CarForm :carData="selectedCar" @submitCar="submitCar" />
    </div>
  </template>
  
  <script>
  import CarForm from '../components/carForm.vue';
  import CarDetail from '../components/carDetail.vue';
  import { mapState } from 'vuex';
  
  export default {
    components: {
      CarForm,
      CarDetail,
    },
    data() {
      return {
        selectedCar: null, // To store the car that is being edited
      };
    },
    computed: {
      ...mapState(['cars']),
    },
    methods: {
      addNewCar() {
        // Reset selectedCar to allow adding a new car
        this.selectedCar = {
          title: '',
          description: '',
          tags: [],
          images: [],
        };
      },
      async submitCar(carData) {
        if (this.selectedCar && this.selectedCar.id) {
          // Update existing car
          await this.$store.dispatch('updateCar', { id: this.selectedCar.id, carData });
        } else {
          // Add new car
          await this.$store.dispatch('addCar', carData);
        }
        this.selectedCar = null; // Clear form after submission
      },
      editCar(car) {
        // Set selectedCar to allow editing
        this.selectedCar = { ...car };
      },
      async deleteCar(carId) {
        await this.$store.dispatch('deleteCar', carId);
      },
    },
    created() {
      // Fetch cars when the component is created
      this.$store.dispatch('fetchCars');
    },
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  .car-card {
    margin-bottom: 20px;
  }
  </style>
  