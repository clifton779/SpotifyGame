import { render, screen } from '@testing-library/react';
import React from 'react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const musicElement = screen.getByTestId('music-player');
  expect(musicElement).toBeInTheDocument();
});

test('renders input field', () => {
  render(<App />);
  const inputElement = screen.getByTestId('input-field');
  expect(inputElement).toBeInTheDocument();
});
