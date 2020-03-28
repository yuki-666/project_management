<template>
  <span class="zx-tag" :class="`zx-tag--${type}`">
    <slot></slot>
  </span>
</template>

<script>
export default {
  name: 'ZxTag',
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
.zx-tag {
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
.zx-tag--primary {
  background: $--color-primary-light;
  color: $--color-primary;
}

.zx-tag--success {
  background: $--color-success-light;
  color: $--color-success;
}

.zx-tag--warning {
  background: $--color-warning-light;
  color: $--color-warning;
}

.zx-tag--danger {
  background: $--color-danger-light;
  color: $--color-danger;
}
</style>
