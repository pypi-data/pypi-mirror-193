//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../../_base/serializers');

var KeyframeTrackModel = require('../KeyframeTrack.autogen.js').KeyframeTrackModel;


class BooleanKeyframeTrackModel extends KeyframeTrackModel {

    defaults() {
        return _.extend(KeyframeTrackModel.prototype.defaults.call(this), {


        });
    }

    constructThreeObject() {

        var result = new THREE.BooleanKeyframeTrack(
            this.get('name'),
            this.convertArrayBufferModelToThree(this.get('times'), 'times'),
            this.convertArrayBufferModelToThree(this.get('values'), 'values'),
            this.convertEnumModelToThree(this.get('interpolation'), 'interpolation')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        KeyframeTrackModel.prototype.createPropertiesArrays.call(this);




    }
}

BooleanKeyframeTrackModel.model_name = 'BooleanKeyframeTrackModel';
BooleanKeyframeTrackModel.serializers = {
    ...KeyframeTrackModel.serializers,
};

module.exports = {
    BooleanKeyframeTrackModel: BooleanKeyframeTrackModel,
};
