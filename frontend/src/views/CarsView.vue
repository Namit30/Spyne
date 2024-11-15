<template>
  <div class="cars-view">
    <h1>My Cars</h1>
    <div class="cars-container">
      <button @click="showAddCarForm = true" class="add-car-button">Add New Car</button>
      <div class="cars-list">
        <div v-for="car in cars" :key="car.id" class="car-card">
          <h3>{{ car.title }}</h3>
          <p>{{ car.description }}</p>
          <div class="car-images">
            <img v-for="(image, index) in car.images" 
                 :key="index" 
                 :src="image" 
                 :alt="car.title"
                 class="car-image">
          </div>
          <div class="car-tags">
            <span v-for="(tag, index) in car.tags" 
                  :key="index" 
                  class="tag">
              {{ tag }}
            </span>
          </div>
          <div class="car-actions">
            <button @click="editCar(car)">Edit</button>
            <button @click="deleteCar(car.id)">Delete</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'CarsView',
  data() {
    return {
      showAddCarForm: false,
    };
  },
  computed: {
    ...mapState(['cars']),
  },
  methods: {
    ...mapActions(['fetchCars', 'deleteCar']),
    editCar(car) {
      // Implement edit functionality
      console.log('Edit car:', car);
    },
  },
  created() {
    this.fetchCars();
  },
};
</script>

<style scoped>
.cars-view {
  padding: 20px;
}

.cars-container {
  max-width: 1200px;
  margin: 0 auto;
}

.add-car-button {
  margin-bottom: 20px;
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.add-car-button:hover {
  background-color: #45a049;
  transform: scale(1.05);
}

.cars-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.car-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  background: white;
  transition: box-shadow 0.3s ease;
}

.car-card:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.car-images {
  display: flex;
  overflow-x: auto;
  gap: 10px;
  margin: 10px 0;
}

.car-image {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 4px;
}

.car-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  margin: 10px 0;
}

.tag {
  background: #e0e0e0;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.9em;
}

.car-actions {
  display: flex;
  gap: 10px;
  margin-top: 10px;
}

button {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  background: #4CAF50;
  color: white;
}

button:hover {
  background: #45a049;
}
</style> 