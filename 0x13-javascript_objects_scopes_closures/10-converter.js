#!/usr/bin/node

exports.converter = function (base) {
  return (baseTen) => {
    return baseTen.toString(base);
  };
};
