<template>
    <form @submit.prevent="handleSubmit">
      <input v-model="car.title" placeholder="Title" required />
      <textarea v-model="car.description" placeholder="Description"></textarea>
  
      <!-- Handle dynamic tags input -->
      <div v-for="(tag, index) in car.tags" :key="index">
        <input v-model="car.tags[index]" placeholder="Tag" />
        <button type="button" @click="removeTag(index)">Remove</button>
      </div>
      <button type="button" @click="addTag">Add Tag</button>
  
      <!-- File upload for images -->
      <input type="file" @change="handleImageUpload" multiple />
      
      <button type="submit">Submit</button>
    </form>
  </template>
  
  <script>
  export default {
    name: 'CarForm', // Multi-word name as per Vue conventions
    props: ['carData'],
    data() {
      return {
        car: this.carData || {
          title: '',
          description: '',
          tags: [],
          images: [],
        },
      };
    },
    methods: {
      // Adds a new empty tag field
      addTag() {
        this.car.tags.push('');
      },
  
      // Removes a tag by index
      removeTag(index) {
        this.car.tags.splice(index, 1);
      },
  
      // Handles file upload
      handleImageUpload(event) {
        this.car.images = [...event.target.files];
      },
  
      // Submit the form data
      handleSubmit() {
        this.$emit('submitCar', this.car);
      },
    },
  };
  </script>
  