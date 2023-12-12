import {describe, expect, test} from '@jest/globals';
import {narcissistic} from '../src/easy';


describe('Testing Narcissistic numbers', () => {
  test('basic tests', () => {
    expect(narcissistic(7)).toBe(true);
    expect(narcissistic(153)).toBe(true);
    expect(narcissistic(487)).toBe(false);
  });
})