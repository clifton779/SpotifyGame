import React from 'react';
import PropTypes from 'prop-types';

export default function Player({ url }) {
  return (
    <audio hidden id="audio" src={url} autoPlay data-testid="music-player" />
  );
}

Player.propTypes = {
  url: PropTypes.string.isRequired,
};
