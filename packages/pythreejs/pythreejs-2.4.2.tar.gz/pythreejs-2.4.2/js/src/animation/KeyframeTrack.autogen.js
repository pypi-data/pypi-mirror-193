//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var ThreeModel = require('../_base/Three.js').ThreeModel;


class KeyframeTrackModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            name: "",
            times: undefined,
            values: undefined,
            interpolation: "InterpolateLinear",

        });
    }

    constructThreeObject() {

        var result = new THREE.KeyframeTrack(
            this.get('name'),
            this.convertArrayBufferModelToThree(this.get('times'), 'times'),
            this.convertArrayBufferModelToThree(this.get('values'), 'values'),
            this.convertEnumModelToThree(this.get('interpolation'), 'interpolation')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);
        this.datawidget_properties.push('times');
        this.datawidget_properties.push('values');

        this.enum_property_types['interpolation'] = 'InterpolationModes';

        this.property_converters['name'] = null;
        this.property_converters['times'] = 'convertArrayBuffer';
        this.property_converters['values'] = 'convertArrayBuffer';
        this.property_converters['interpolation'] = 'convertEnum';


    }
}

KeyframeTrackModel.model_name = 'KeyframeTrackModel';
KeyframeTrackModel.serializers = {
    ...ThreeModel.serializers,
    times: dataserializers.data_union_serialization,
    values: dataserializers.data_union_serialization,
};

module.exports = {
    KeyframeTrackModel: KeyframeTrackModel,
};
