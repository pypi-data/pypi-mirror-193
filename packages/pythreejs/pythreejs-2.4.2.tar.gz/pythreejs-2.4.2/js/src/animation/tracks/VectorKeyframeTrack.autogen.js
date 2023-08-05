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


class VectorKeyframeTrackModel extends KeyframeTrackModel {

    defaults() {
        return _.extend(KeyframeTrackModel.prototype.defaults.call(this), {


        });
    }

    constructThreeObject() {

        var result = new THREE.VectorKeyframeTrack(
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

VectorKeyframeTrackModel.model_name = 'VectorKeyframeTrackModel';
VectorKeyframeTrackModel.serializers = {
    ...KeyframeTrackModel.serializers,
};

module.exports = {
    VectorKeyframeTrackModel: VectorKeyframeTrackModel,
};
