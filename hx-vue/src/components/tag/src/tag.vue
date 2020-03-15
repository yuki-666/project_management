<template>
  <span class="xm-tag" :class="`xm-tag--${type}`">
    <slot></slot>
  </span>
</template>

<script>
export default {
  name: 'XmTag',
  props: {
    type: {
      type: String,
      default: ''
    }
  }
}
</script>
<style lang="scss">
$--color-primary: #2672ff !default;
$--color-success: #5ec976 !default;
$--color-warning: #fab55a !default;
$--color-danger: #fa7070 !default;

$--color-primary-light: #e9f0ff !default;
$--color-success-light: #eef9f1 !default;
$--color-warning-light: #fdf6ea !default;
$--color-danger-light: #fff0f0 !default;
.xm-tag {
  font-size: 12px;
  line-height: 1;
  padding: 4px 5px;
  background: #fff;
  color: #666;
  display: inline-block;
  box-sizing: border-box;
  white-space: nowrap;
  border-radius: 2px;
}
.xm-tag--primary {
  background: $--color-primary-light;
  color: $--color-primary;
}

.xm-tag--success {
  background: $--color-success-light;
  color: $--color-success;
}

.xm-tag--warning {
  background: $--color-warning-light;
  color: $--color-warning;
}

.xm-tag--danger {
  background: $--color-danger-light;
  color: $--color-danger;
}
</style>
