/**
 * @return {null|boolean|number|string|Array|Object}
 */

// Memory: 42.02MB, Beats: 12.54% of users with JavaScript
Array.prototype.last = function() {
  const num = this.length;
  let result = -1;
  if (num) {
      result = this[num - 1];
  }
  return result;
};
